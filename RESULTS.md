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
    - read = 404
    - change = 400
    - delete = 400

## Part B
1. One is the flaky login that we found in step 0.16, another one is when we found defect where we expect 400 but then got 500 instead. The stub would not find them like us. Reason to write unit tests with stub are that they are quick and they dont rely on network.
2. Since its a shared public token, someone might accidently delete or change something during the run, and may cause problem to not see the reall result. In project 2 we should create our own data so it doesnt interfere with what other groups do.
3. There are many servers and each one keep its own user, so the session keep the cookieand send request to the same server. IN step 0.12 all three runs failed for me.
4. The block is all three tools excluded. 500 with empty body is worse because you dont know what exact the error is as there is no body to tell you. A 400 with error message can tell you more about what the issue is. It is kept so that we can see it while the suite stays green, and remind us to go back to remove it.
5. Base choice = 1 base + num of blocks - 1 for each characteristics. 1 + 2 + 3 + 1 + 2 = 9. All combination = multply num of block. 3 x 4 x 2 x 3 = 72.
6. Step A4 i got 404, 400, 400. I would expect maybe 403 or 404. I think it seems ok since the rating didn't change, but it might be a small defect, also the result are not so consistent.
7. I got this back: HTTP/2 401 {"error":"authentication failed"}. I don't think its a defect, and the stranger might skip login and interfere with the data.
8. API would be better at doing things that the web did not meant to be done, like sending text instead of number or something our of range. Web page would be better at what user can see, like error message popup alert.
