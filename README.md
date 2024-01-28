# reloading-tool

This tool is meant as a way to document and analyze my own load testing results so that future load development can 
start closer to an optimal load.

The goal is to build a statistical model of what combination of variables results in a "good load". For the purposes of 
this tool, a load is considered good when standard deviation and extreme spread are as close to single digits as possible
or when the load produces a sub moa group.

In addition to a statistical model, calculations such as the "Optimal Barrel Time" will be computed to give a higher 
confidence in a good load.