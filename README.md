# Temporal signal with Phytest

In this example we use [phytest]() to enure that there is temporal signal in a dataset of sequences sampled through time. Temporal signal analysis is an important step for detecting problematic sequences and potential issues before heading on to a Bayesian phylogenetic analysis (e.g. with [BEAST](https://beast.community/beast)). 

This example uses data from the [TempEst tutorial](https://beast.community/tempest_tutorial). TempEst is a useful program for explore a temporal signal analysis though a GUI, however, it is not possible to automate TempEst. Under the hood Phytest uses [TimeTree](https://github.com/neherlab/treetime) to perform root-to-tip regression allowing us to automate temporal signal testing. Automating this process is especially useful when an analysis is run many times e.g. through development or during daily builds. 

## Setup

Create a python environment

```bash
python3 -m venv venv
```

Activate the environment

```bash
source venv/bin/activate
```

Install `phytest` with pip

```bash
python -m pip install phytest
```

## Tests

In the `ice_viruses_tests.py` file we define the tests that we want to run on our dataset. Phytest is a flexible framework that provides many built in tests and is easily extendable. For simplicity we will focus on a small test set but see the phytest docs for more information. 

The focus of this test will be determining if the dataset meets our temporal signal requirements. in the file we file the test below. We want the r squared value of our root-to-tip regression to be greater that 0.5 (this suggest a strong correlation between branch length and sampling date), we want the inferred rate to be between 0.001 and 0.01 (the evolutionary rate of influenza is on the order of 10^-3), and finally we expect the root date i.e. TMRCA to be in the 19th century. We also add some simple tests for the sequence length and 

```
def test_root_to_tip(tree: Tree):
    tree.assert_root_to_tip(
        min_r_squared=0.5, 
        min_rate=0.001, 
        max_rate=0.01, 
        min_root_date=1800, 
        max_root_date=1900
    )
```

If these test do not pass then then phytest will fail. While these test aren't very strict (we give our-selves a lot of wiggle room) they are still useful for picking up errors before the analysis is run. 

## Data

Here we test two data sets from the [TempEst tutorial](https://beast.community/tempest_tutorial). The fist is a uncleaned dataset that contains erroneous data and the seconds is a cleaned dataset that has the sequences removed.

### Uncleaned 

```pash
phytest ice_viruses_tests.py -a data/ice_viruses.fasta -t data/ice_viruses.fasta.treefile
```

From the output we can see that out tests failed because the R-squarred value from the root-to-tip regression is less than 0.5.

```
Test session starts (platform: darwin, Python 3.8.5, pytest 7.1.2, pytest-sugar 0.9.4)
rootdir: /Users/wytamma/programming/phytest-temporal-signal-example
plugins: metadata-2.0.1, html-3.1.1, sugar-0.9.4
collecting ... 
 ice_viruses_tests.py ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓   98% █████████▊

 ice_viruses_tests.py ⨯                                                      100% ██████████
===================================== short test summary info ========================
FAILED ice_viruses_tests.py::test_root_to_tip[tree0] - phytest.utils.PhytestAssertion: The 
R-squarred value from the root-to-tip regression '0.36462497968641333' is less than '0.5'.

Results (0.31s):
      53 passed
       1 failed
         - ice_viruses_tests.py:12 test_root_to_tip[tree0]
```
### Cleaned 

```bash
phytest ice_viruses_tests.py -a data/ice_viruses_cleaned.fasta -t data/ice_viruses_cleaned.fasta.treefile
```

Using the cleaned dataset all our tests pass, giving us confidence to progress with our analysis. 

```
rootdir: /Users/wytamma/programming/phytest-temporal-signal-example
plugins: metadata-2.0.1, html-3.1.1, sugar-0.9.4
collecting ... 
 ice_viruses_tests.py ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓    100% ██████████

Results (0.34s):
      47 passed
```
