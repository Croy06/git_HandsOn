# seqClass.py

This script classifies a given sequence as either DNA or RNA.

## Usage

```bash
python3 seqClass.py -s <sequence> [-m <motif>]
```

## Arguments

- `-s`, `--seq`: The input sequence. This argument is mandatory.
- `-m`, `--motif`: A motif to search for within the sequence. This argument is optional.

## Examples

```bash
python3 seqClass.py -s ATCG
```

This command will classify the sequence `ATCG` as either DNA or RNA.

```bash
python3 seqClass.py -s AUG -m UG
```

This command will classify the sequence `AUG` as either DNA or RNA and will search for the motif `UG` within the sequence.

## Notes

- Sequences should only contain the characters `A`, `C`, `G`, `T`, and/or `U`.
- Both sequences and motifs are case-insensitive.
