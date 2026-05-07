# GenLayer AI Grant Reviewer

A GenLayer Intelligent Contract that uses AI non-determinism to review grant proposals.

## What it does

The contract accepts a grant proposal and returns:

- score from 1 to 10
- decision: approve, revise, or reject
- strength
- risk
- suggestion

## GenLayer features used

- `gl.nondet.exec_prompt`
- `gl.vm.run_nondet_unsafe`
- validator function for JSON output
- public write method: `review_proposal`
- public view method: `get_last_review`

## Smart Contract

The smart contract code is included in this repository:

- `ai_grant_reviewer.py`

## Test proposal

Build a GenLayer dApp that uses AI to review grant proposals and returns a score, decision, risks, and suggestions.

## Status

Deployed and tested successfully in GenLayer Studio.

## Contract address

0x264800e1bFF52b0cD639b740110AC51f134AfC4e
