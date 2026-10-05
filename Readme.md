# NIST Test Suite Setup on WSL

## Steps

1. First, open **WSL** from Search.

2. Change the directory to the folder where the file is present for which you have to run the **NIST Test Suite**.

   Example:

   ```bash
   cd "/mnt/c/Quantum MTech_1_8_2026/TEst2"
   ```

   **Generic command (use your own path):**

   ```bash
   cd "/mnt/c/path/to/your/NIST-test-folder"
   ```

   > **Note:** Replace the path inside the quotes with the actual location of your folder.  
   > Keep the quotes if the path contains spaces.  
   > In WSL, your Windows `C:` drive is mounted at `/mnt/c`.

   This command will move your WSL (Windows Subsystem for Linux) terminal to the desired folder `TEst2`.


3. 
### 3.1 Update Ubuntu package information

```bash
sudo apt update
```

This refreshes Ubuntu's package information.

### 3.2 Install build tools and Git

```bash
sudo apt install -y build-essential git
```

Meaning:

> Install Git and the essential tools required to build/compile software, using administrator privileges and automatically confirming the installation.  


### 3.4 Go to the Linux home directory

```bash
cd ~
```

### 3.5 Clone the NIST STS Repository

```bash
git clone https://github.com/terrillmoore/NIST-Statistical-Test-Suite.git nist-sts
```

**Meaning:**
> Try to download the NIST Statistical Test Suite from GitHub.

### 3.6 Enter the NIST-STS folder

```bash
cd nist-sts
```

**Meaning:**
> Enter the existing NIST-STS folder.

### 3.7 Run the setup script

```bash
./setup.sh
```

**Meaning:**
> Run the project's setup script.
> - It checks/creates the required folders and experiment directories.

### 3.8 Enter the STS directory

```bash
cd ./sts
```

**Meaning:**
> Enter the `sts` folder where the NIST test program is located.

### 3.9 Build NIST STS

```bash
make
```

**Meaning:**
> Compile/build the NIST STS program.

If the terminal says:

```text
make: 'assess' is up to date.
```

the executable is already built and ready.

## Part 2: Running NIST STS on a New Dataset

Once NIST STS has already been installed, the workflow for every new binary dataset is short.

### Step 1 — Enter the STS directory

```bash
cd ~/nist-sts/sts
```

### Step 2 — Copy the dataset from Windows

**Example:**

```bash
cp "/mnt/c/Quantum MTech_1_8_2026/TEst2/csprng_dataset_imb.bin" csprng_dataset_imb.bin
```

The structure is:

```text
cp SOURCE DESTINATION
```

For the example:

```text
SOURCE:
/mnt/c/Quantum MTech_1_8_2026/TEst2/csprng_dataset_imb.bin

DESTINATION:
csprng_dataset_imb.bin
```

> **Note:** The destination is the copy placed in the current NIST `sts` directory.

### Step 3 — Start the NIST Statistical Test Suite

Start the NIST Statistical Test Suite and tell it that the input sequence contains 1,000,000 bits.

```bash
./assess 1000000
```

> **Note:** The number `1000000` represents the bit length of your input sequence. Adjust this number if your dataset contains a different number of bits.


 **NIST Recommendation for Sequence Length**

> **Note:** NIST recommends that each sequence contain at least 1,000,000 bits:
> \(n \ge 10^6\) bits.


## Part 3: Running the Tests & Analyzing Results

### 8. Interactive NIST Settings

For a binary dataset, use the following settings.

**Generator Selection**

When NIST displays:
```text
[0] Input File
[1] Linear Congruential
...
```

Enter:
```text
0
```

**Meaning:**
> Use our own input file.

**Run all statistical tests**

When NIST asks whether to apply all statistical tests:

Enter Choice:
```text
1
```

**Meaning:**
> Run all 15 statistical tests.

**Parameter adjustments**

When NIST displays the test parameters and asks:
```text
Select Test (0 to continue):
```

Enter:
```text
0
```

**Meaning:**
> Continue using the displayed/default parameter settings.

**Number of bitstreams**

Enter the number calculated from your dataset size.
*For example, for an exactly 1 MB decimal file:*
```text
8
```

**Input format**

When NIST asks:
```text
[0] ASCII
[1] Binary
```

Enter:
```text
1
```

**Meaning:**
> The input file is binary; each byte contains 8 bits of data.


### 9. The 15 NIST Statistical Tests

When all tests are selected, NIST STS evaluates:

1. Frequency
2. Block Frequency
3. Cumulative Sums
4. Runs
5. Longest Run of Ones
6. Rank
7. Discrete Fourier Transform (FFT)
8. Non-Overlapping Template Matching
9. Overlapping Template Matching
10. Universal Statistical
11. Approximate Entropy
12. Random Excursions
13. Random Excursions Variant
14. Serial
15. Linear Complexity

These tests examine different statistical properties of the binary sequence.



### 10. Finding the Final Report

After the test finishes, search for report files:

```bash
find experiments/ -name "*Report*.txt" -o -name "finalAnalysisReport.txt"
```

**Example output:**
```text
experiments/AlgorithmTesting/finalAnalysisReport.txt
```

### 11. Viewing the Report in the Terminal

For the `AlgorithmTesting` report:

```bash
cat experiments/AlgorithmTesting/finalAnalysisReport.txt
```

For a long report:

```bash
less experiments/AlgorithmTesting/finalAnalysisReport.txt
```

Press `q` to exit `less`.

### 12. Copying the Final Report to Windows

Use:

```bash
cp experiments/AlgorithmTesting/finalAnalysisReport.txt "/mnt/c/Quantum MTech_1_8_2026/TEst2/basic_prng_NIST_report.txt"
```

The command structure is:
```text
cp SOURCE DESTINATION
```

**Source:**
```text
experiments/AlgorithmTesting/finalAnalysisReport.txt
```

**Destination:**
```text
/mnt/c/Quantum MTech_1_8_2026/TEst2/basic_prng_NIST_report.txt
```

The file will appear in Windows as:
```text
C:\Quantum MTech_1_8_2026\TEst2\basic_prng_NIST_report.txt
```

### 13. Preserve the Complete NIST Results

The final report is a summary. It is recommended to preserve the complete experiment output as well.

For example:

```bash
cp -r experiments/AlgorithmTesting "/mnt/c/Quantum MTech_1_8_2026/TEst2/basic_prng_NIST_results"
```

For another generator:

```bash
cp -r experiments/AlgorithmTesting "/mnt/c/Quantum MTech_1_8_2026/TEst2/csprng_NIST_results"
```

> **Note:** Use a unique destination name for each generator so previous results are not overwritten.

### 14. Recommended Project Folder Structure

A clean structure is:

```text
TEst2/
│
├── basic_prng/
│   ├── basic_prng_1mb.bin
│   ├── basic_prng_NIST_Report.txt
│   └── basic_prng_NIST_results/
│
├── csprng/
│   ├── csprng_dataset_1mb.bin
│   ├── csprng_NIST_Report.txt
│   └── csprng_NIST_results/
│
├── qrng/
│   ├── qrng_dataset_1mb.bin
│   ├── qrng_NIST_Report.txt
│   └── qrng_NIST_results/
│
└── README.md
```

This makes it easy to compare different generators.