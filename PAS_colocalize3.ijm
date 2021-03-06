rename("Fig");
run("Split Channels");
selectWindow("C1-Fig");
rename("Atg17");
selectWindow("C2-Fig");
rename("Atg");
selectWindow("Atg17");
run("Find Maxima...", "noise=2000 output=[Single Points] exclude");
run("Maximum...", "radius=1");
selectWindow("Atg");
run("Find Maxima...", "noise=3000 output=[Single Points] exclude");
run("Maximum...", "radius=1");
imageCalculator("Multiply create", "Atg17 Maxima","Atg Maxima");
selectWindow("Result of Atg17 Maxima");
selectWindow("Atg17 Maxima");
run("Find Maxima...", "noise=1 output=Count exclude");
selectWindow("Result of Atg17 Maxima");
run("Find Maxima...", "noise=1 output=Count exclude");
run("Close All");