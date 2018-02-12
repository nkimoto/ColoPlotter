#!/usr/bin/python
# -*- Coding: utf-8 -*-

from skimage import io
from skimage import img_as_float
from skimage.color import rgb2gray
from matplotlib import pyplot as plt
import os
import argparse
import numpy as np


def read_input(input_dir):
    """
    input dir need to contain TIF files
    output : img generater
    """
    files = os.listdir(input_dir)
    for f in files:
        img = io.imread(os.path.join(input_dir, f))
        yield (img[0], img[1])


def ThresholdGetter(img_f, threshold_p, search_gap):
    size = img_f.size
    threshold_num = size * threshold_p / 100
    print(size)
    print(threshold_num)
    for i in np.arange(1, 0, -1 * search_gap):
        more = img_f > i
        passed_pixel = len(more[more == 1])
        if passed_pixel > 0:
            print('Threshold(intensity) : {}'.format(i))
            print('passed_pixel : {}'.format(passed_pixel))
            if len(more[more == 1]) > threshold_num:
                return i


def ColoPlotter(input_dir, output_dir, name1, name2, threshold_p, search_gap, denominator):
    print(input_dir)
    mrate1_list = np.array([])
    mrate2_list = np.array([])
    for n, (img1, img2) in enumerate(read_input(input_dir)):
        # RGB to Grey and Merge
        grey1 = rgb2gray(img1)
        grey2 = rgb2gray(img2)
        img_f1 = img_as_float(grey1)
        img_f2 = img_as_float(grey2)
        more1 = img_f1 > ThresholdGetter(img_f1, threshold_p, search_gap)
        more2 = img_f2 > ThresholdGetter(img_f2, threshold_p, search_gap)
        merge = more1 * more2
        mrate1 = len(merge[merge == 1])/len(more1[more1 == 1]) * 100
        mrate2 = len(merge[merge == 1])/len(more2[more2 == 1]) * 100
        mrate1_list = np.append(mrate1_list, mrate1)
        mrate2_list = np.append(mrate2_list, mrate2)


        # Make Figure
        fig, axes = plt.subplots(figsize=(10, 10), nrows=2, ncols=3, subplot_kw={'adjustable': 'box-forced'})
        axes[0, 0].imshow(img1)
        axes[0, 0].set_title(name1)
        axes[1, 0].imshow(img2)
        axes[1, 0].set_title(name2)
        axes[0,1].imshow(more1)
        axes[1,1].imshow(more2)
        axes[0,2].imshow(merge)
        axes[1,2].imshow(merge)
        if os.path.exists(output_dir) is False:
            os.makedirs(output_dir)
        fig.savefig(os.path.join(output_dir, '{}_{}_{}_{}.png'.format(name1, name2, threshold_p, n + 1)))

    else:
        print('Merge Rates (denominator = {}) : '.format(name1), end="")
        print(mrate1_list)
        sigma1 = mrate1_list.std()
        print('standard deviation = %f'% sigma1)
        print('Merge Rates (denominator = {}) : '.format(name2), end="")
        print(mrate2_list)
        sigma2 = mrate2_list.std()
        print('standard deviation = %f'% sigma2)

        #Make Graph
        left = np.array([1])
        plt.figure(figsize=(2,4))
        plt.style.use('ggplot')
        if denominator == '1':
            height = np.array([mrate1_list.mean()])
            sigma = sigma1
            label = [name2]
            plt.ylabel('% Colocalization\nwith {}'.format(name1))
        else:
            height = np.array([mrate2_list.mean()])
            sigma = sigma2
            label = [name1]
            plt.ylabel('Colocalization\nwith {}'.format(name2))
        # plt.title('Colocalization')
        plt.ylim(ymax = 100.0, ymin = 0)
        plt.xlim(xmax = 2.0, xmin = 0)
        plt.bar(left, height, width=1, yerr=sigma, tick_label=label,capsize=10)
        if denominator == 1:
            plt.savefig(os.path.join(output_dir, "{}_{}_{}_bar.png".format(name1, name2, str(threshold_p))), format='png', bbox_inches='tight')
        else:
            plt.savefig(os.path.join(output_dir, "{}_{}_{}_bar.png".format(name2, name1, str(threshold_p))), format='png', bbox_inches='tight')


def ArgParse():
    parser = argparse.ArgumentParser(description='Get Colocalization Rate')
    parser.add_argument('-d', '--denominator',
                         dest='denominator',
                         choices=['1', '2'],
                         default='1',
                         help='Choose denominator "1" or "2".')
    parser.add_argument('-t', '--threshold',
                        dest='threshold',
                        type=float,
                        default=5.0,
                        help='Threshold : Least pixel number(%).')
    parser.add_argument('-n1', '--name1',
                        dest='name1',
                        default='sample1',
                        help='Name1(TIF[1])')
    parser.add_argument('-n2', '--name2',
                        dest='name2',
                        default='sample2',
                        help='Name2 (TIF[1])')
    parser.add_argument('-sg', '--search_gap',
                        dest='sg',
                        type=float,
                        default=0.001,
                        help='You can specify "search gap" (default = 0.001).\
                        This script search threshold by "search gap" from 1 to 0.')
    parser.add_argument('-in', '--input_dir',
                        dest='in_dir',
                        required=True,
                        help='You need to specify input dir.')
    parser.add_argument('-out', '--output_dir',
                        dest='out_dir',
                        default='result',
                        help='You can specify output dir.')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = ArgParse()
    ColoPlotter(input_dir=args.in_dir,
                output_dir=args.out_dir,
                name1=args.name1,
                name2=args.name2,
                threshold_p=args.threshold,
                search_gap=args.sg,
                denominator=args.denominator)

