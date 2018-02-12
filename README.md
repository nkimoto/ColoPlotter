# ColoPlotter
Calculate colocalization by max intensity.

ImageJ's macro (PAS_colocalize3.ijm) by Python

## Method 
Convert intensity to float  
→ image thresholding by Max intensity   
→ Merge sample1 with sample2  
→ Calculate colocalization rate (Error bar is *standard deviation*)  
→ Output figures


## Usage
```
ColoPlotter.py -d 1 -t 90.0 -n1 protein1 -n2 protein2 -sg 0.001 -in /path/to/input_dir -out /path/to/out_dir
```

## Options 

| OptionName | Default | Descrioption |
|:-----------|:------------:|:------------|
| `-d`, `--denominator` | `1` | Which one do you want to set to denominator (`1` : 1st or `2` : 2nd). |
| `-t`, `--threshold` | `90.0` | Set threshold to the percentage of Max Intensity (%) |
| `-n1`, `name1` | `sample1` | Set the 1st protein name of the figure(Tif)|
| `-n2`, `name2` | `sample2` | Set the 2nd proitein name of the figure(Tif)|
| `-sg`, `--search_gap` | `0.001` | ColoPlotter.py sarch the threshold by this gap. |
| `-in`, `--input_dir` | required | Input directory. The directory need to contain multiple figures(Tif). |
| `-out`, `--output_dir` | `result` | Output directory. Result png files are made in the specified directory. |

## Example
### command
```
python ColoPlotter.py -in C:\Users\Win10\Documents\test\PGSM_16 -n1 Pep1 -n2 Sec7 -sg 0.00001 -out result\PGSM_16 -t 60
```

### Output
#### Standard output
```
Merge Rates (denominator = Pep1) : [  4.34782609  43.28358209  12.13235294  18.18181818  27.94117647]
standard deviation = 13.479265
Merge Rates (denominator = Sec7) : [  2.22222222  78.37837838  75.          22.22222222  27.53623188]
standard deviation = 30.300863
```
#### output figures 
Figure 1  
<img src="https://github.com/nkimoto/ColoPlotter/blob/number_th/example/PGSM_16/Pep1_Sec7_5.0_1.png" alt="ex1" title="ex1" width="400px">  

Figure 2  
<img src="https://github.com/nkimoto/ColoPlotter/blob/number_th/example/PGSM_16/Pep1_Sec7_5.0_2.png" alt="ex2" title="ex1" width="400px">  

Figure 3 (high background)  
<img src="https://github.com/nkimoto/ColoPlotter/blob/number_th/example/PGSM_16/Pep1_Sec7_5.0_3.png" alt="ex3" title="ex1" width="400px">  

Figure 4  
<img src="https://github.com/nkimoto/ColoPlotter/blob/number_th/example/PGSM_16/Pep1_Sec7_5.0_4.png" alt="ex4" title="ex1" width="400px">  

Figure 5  
<img src="https://github.com/nkimoto/ColoPlotter/blob/number_th/example/PGSM_16/Pep1_Sec7_5.0_5.png" alt="ex5" title="ex1" width="400px">  

Colocalization Rate Figure  
<img src="https://github.com/nkimoto/ColoPlotter/blob/number_th/example/PGSM_16/Sec7_Pep1_5.0_bar.png" alt="ex5" title="ex1" width="400px">
