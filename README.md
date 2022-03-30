# Volatility CSV Exporter
Final Project for Graduate Seminar

## Description
Volatility as an open-source tool for volatile memory analysis. It consists of a single, cohesive framework that analyzes Random Access Memory (RAM) dumps for 32/64 bit Windows, Linux, Mac, and even android systems [1]. The output from the tool depends on the use of the several plugins that can be used in association with the tool. Volatility as an open-source tool for volatile memory analysis. It consists of a single, cohesive framework that analyzes Random Access Memory (RAM) dumps for 32/64 bit Windows, Linux, Mac, and even android systems [1]. The framework is implemented in Python and used to analyze crash dumps, raw dumps, VMware, and in our case Sandbox dumps. Since this tool analyzes the dumps that result from malicious activity on a system, it is generalized as a dynamic analysis tool. This is because it is used after the malware is executed in the testing environment. The output from the tool depends on the use of the several plugins that can be used in association with the tool.

## Usage
1. Download the ZIP file and unzip
2. Run volatility command (see github below for usage) with ouput flag set to csv (`--output=csv`)

## References
[1] Case, Andrew. “Volatilityfoundation/Volatility.” GitHub, VolatilityFoundation, github.com/volatilityfoundation/volatility/wiki.
