# API lab results
## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: An Orange Margherita
- Step 0.12, results of the three runs without a session (optional): 
    - Run #1: failed
    - Run #2: failed
    - Run #3: failed
- Step 0.16, blocks of "how many of the three tools are excluded": 
    - Block 1: no tools exclued
    - Block 1: one tool excluded
    - Block 2: two tools excluded
    - Block 3: all three tools excluded

## Defect report
- Title: Excluding all tools return 500 with empty body, not 400 
- Request: POST https://quickpizza.grafana.com/api/pizza, {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}
- Expected result: 400 with error message
- Actual result: 500 with no body
- Severity: High, because it error 500 but no message so customer will be confused
## Part A
- Step A4, status codes when the other user reads, changes and deletes:
    - 404
    - 400
    - 400
## Part B
1.
2.
3.
4. 
5. 
6. 
7. 
8.
