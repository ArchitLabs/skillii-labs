# Our team's Python style guide

These are the rules every pull request is reviewed against. Each rule has a number, a short name and the reason behind it.

## Rule 1: Name things for what they mean

Use full words for names that live longer than a few lines. A variable called invoice_total tells the next reader what it holds; a variable called t makes them scroll up and guess. Short names are fine for loop counters and for values used once on the next line.

In review, a comment that cites this rule should name it as 'rule 1' and point to the exact line it applies to.

## Rule 2: One function, one job

A function should do one thing you can describe in a short sentence without the word 'and'. If the sentence needs 'and', split the function. Small functions are easier to test, easier to name, and easier to delete when the requirement changes.

In review, a comment that cites this rule should name it as 'rule 2' and point to the exact line it applies to.

## Rule 3: Keep functions short

Aim for functions that fit on one screen. Long functions hide their structure: a reader has to hold too much in their head at once. When a function grows past forty lines, look for a block you can name and move out.

In review, a comment that cites this rule should name it as 'rule 3' and point to the exact line it applies to.

## Rule 4: Return early

Handle the special cases first and return. Guard clauses at the top keep the main path of the function flat and readable, instead of burying it three levels deep inside if statements.

In review, a comment that cites this rule should name it as 'rule 4' and point to the exact line it applies to.

## Rule 5: Make errors loud

Never swallow an exception silently. If you catch an error, either handle it fully or raise it again with more context. A bare except that passes hides bugs until they reach a customer.

In review, a comment that cites this rule should name it as 'rule 5' and point to the exact line it applies to.

## Rule 6: Write the error message for the person who will read it

An error should say what went wrong, with which value, and what to do next. 'Invalid input' helps nobody; 'quantity must be a positive whole number, got -3' tells the caller exactly what to fix.

In review, a comment that cites this rule should name it as 'rule 6' and point to the exact line it applies to.

## Rule 7: Prefer plain data

Pass dictionaries, tuples and small data classes between functions rather than objects full of hidden state. Plain data is easy to print, easy to compare in a test, and easy to send over the network.

In review, a comment that cites this rule should name it as 'rule 7' and point to the exact line it applies to.

## Rule 8: Type hints on public functions

Every function other modules call gets type hints on its parameters and its return value. Hints are documentation the tools can check, and they catch a whole class of mistakes before the code runs.

In review, a comment that cites this rule should name it as 'rule 8' and point to the exact line it applies to.

## Rule 9: Docstrings say why, not how

A docstring explains what the function is for and anything surprising about it. The code already says how it works; repeating that in prose only creates two things that can drift apart.

In review, a comment that cites this rule should name it as 'rule 9' and point to the exact line it applies to.

## Rule 10: No magic numbers

Give every meaningful number a name. TIMEOUT_SECONDS = 30 explains itself; a bare 30 in the middle of a call does not, and the next person to change it will miss the other three places it appears.

In review, a comment that cites this rule should name it as 'rule 10' and point to the exact line it applies to.

## Rule 11: Configuration comes from the environment

Secrets, endpoints and limits come from environment variables or a configuration file, never from the code. The same code should run on a laptop, in a test and in production with only its environment changed.

In review, a comment that cites this rule should name it as 'rule 11' and point to the exact line it applies to.

## Rule 12: Never commit a secret

API keys, passwords and tokens never enter the repository, not even for a moment and not even in a test. Read them from the environment. If one is committed by mistake, rotate it at once: deleting the commit is not enough.

In review, a comment that cites this rule should name it as 'rule 12' and point to the exact line it applies to.

## Rule 13: Log events, not noise

A log line records something that happened and the values that matter: what, to which record, and how long it took. Avoid logging inside tight loops, and never log a secret or a person's private data.

In review, a comment that cites this rule should name it as 'rule 13' and point to the exact line it applies to.

## Rule 14: Tests come with the change

A change that alters behaviour comes with a test that would have failed before it. The test is part of the change, reviewed with it, and it documents the behaviour for the next person.

In review, a comment that cites this rule should name it as 'rule 14' and point to the exact line it applies to.

## Rule 15: Test behaviour, not implementation

A good test checks what a function promises, not how it does it. Tests tied to internal details break every time the code is tidied, and teams learn to ignore them.

In review, a comment that cites this rule should name it as 'rule 15' and point to the exact line it applies to.

## Rule 16: Keep tests fast

The whole unit test suite should run in seconds. Slow tests get skipped. Anything that needs the network, a database or a real model belongs in a separate, clearly marked suite.

In review, a comment that cites this rule should name it as 'rule 16' and point to the exact line it applies to.

## Rule 17: Dependencies are a cost

Every new package is code you did not write and must now trust, update and audit. Add one only when it saves real work, pin its version, and prefer the standard library for small jobs.

In review, a comment that cites this rule should name it as 'rule 17' and point to the exact line it applies to.

## Rule 18: Format automatically

Formatting is decided by the formatter, not in review. Run it before every commit so reviews can spend their time on behaviour, names and design.

In review, a comment that cites this rule should name it as 'rule 18' and point to the exact line it applies to.

## Rule 19: Small commits, clear messages

Each commit does one thing and says what and why in its message. A reviewer should be able to read the history like a short story of the change.

In review, a comment that cites this rule should name it as 'rule 19' and point to the exact line it applies to.

## Rule 20: Review for the reader

In review, ask whether someone new to this code could understand it next month. If you had to read a line twice, say so: that line needs a better name or a comment.

In review, a comment that cites this rule should name it as 'rule 20' and point to the exact line it applies to.

## Rule 21: Measure before optimising

Do not make code faster on a hunch. Measure where the time goes, change the slow part, and measure again. Most code is fast enough, and clear code is easier to speed up later.

In review, a comment that cites this rule should name it as 'rule 21' and point to the exact line it applies to.

## Rule 22: Budget your model calls

Every call to a language model costs money by the token, both for what you send and for what it writes. Count tokens before you ship a feature, cap the length of answers, and log the usage each response reports.

In review, a comment that cites this rule should name it as 'rule 22' and point to the exact line it applies to.

## Rule 23: Send only what the model needs

Input tokens are billed on every request. Trim long documents to the relevant part, do not resend data the model does not need, and remember that in a chat the whole history is sent again on every turn.

In review, a comment that cites this rule should name it as 'rule 23' and point to the exact line it applies to.

## Rule 24: Reuse stable instructions

Keep long, stable instructions at the start of the prompt and the changing parts at the end, so prompt caching can reuse the opening. Do not put timestamps or user names in the opening, or the cache will never match.

In review, a comment that cites this rule should name it as 'rule 24' and point to the exact line it applies to.

## Rule 25: Handle model errors like network errors

A model call can time out, be rate-limited or return an error. Retry with backoff for temporary failures, give up cleanly after a few tries, and never retry in a tight loop that multiplies your bill.

In review, a comment that cites this rule should name it as 'rule 25' and point to the exact line it applies to.

## Rule 26: Check what the model returns

Treat a model's output as untrusted input. Validate its shape before you use it, never execute it blindly, and have a fallback when it does not match what you asked for.

In review, a comment that cites this rule should name it as 'rule 26' and point to the exact line it applies to.

## Rule 27: Keep humans in the loop for risky actions

If the model's answer would delete data, spend money or contact a customer, a person confirms it first. Automation is for the safe, reversible steps.

In review, a comment that cites this rule should name it as 'rule 27' and point to the exact line it applies to.

## Rule 28: Document the decisions

When you choose between two reasonable designs, write down which one and why, next to the code. The next person will otherwise repeat the debate, or undo the choice without knowing the reason.

In review, a comment that cites this rule should name it as 'rule 28' and point to the exact line it applies to.
