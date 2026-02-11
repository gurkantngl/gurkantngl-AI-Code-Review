# AI Code Review Assignment (Python)

## Candidate

- Name: Gürkan Töngel
- Approximate time spent: 30 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings

### Critical bugs

- Uses total order count as the denominator while excluding cancelled orders from the numerator, so the average is incorrect.
- Raises `ZeroDivisionError` when `orders` is empty or when all orders are cancelled.

### Edge cases & risks

- Empty input list.
- All orders cancelled.
- Missing or non-numeric `amount` / missing `status` will raise at runtime (not handled).

### Code quality / design issues

- Count should reflect only included orders, not the full list length.
- No explicit behavior defined for zero valid orders.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Track count of non-cancelled orders while summing.
- Guard against zero valid orders by returning `0`.

### Corrected code

See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

- Empty list and all-cancelled list to ensure no division by zero.
- Mixed cancelled and non-cancelled orders to verify correct averaging.
- Single valid order and floating/negative amounts to confirm arithmetic.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation

- It claims the denominator excludes cancelled orders; the code uses `len(orders)` instead.
- It ignores the division-by-zero risk for empty or all-cancelled inputs.

### Rewritten explanation

- Sums the `amount` for orders whose `status` is not `"cancelled"` and divides by the count of those orders. If there are no non-cancelled orders, it returns `0` instead of raising an error.

## 4) Final Judgment

- Decision: Request Changes
- Justification: The current implementation computes an incorrect average and can crash on empty or all-cancelled inputs.
- Confidence & unknowns: High. Business rule for "no valid orders" is assumed to return `0`.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings

### Critical bugs

- Counts many invalid emails as valid (e.g., strings with multiple `@` or missing local/domain parts).
- Raises `TypeError` when a non-string entry (e.g., `None`) is encountered because it uses `"@" in email`.

### Edge cases & risks

- Emails with leading/trailing whitespace.
- Multiple `@` symbols or empty local/domain parts.
- Non-string items in the list.

### Code quality / design issues

- Validation rule is too weak to match the "valid email" requirement.
- No basic type checking or normalization.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Ignore non-string inputs safely.
- Require exactly one `@` and non-empty local and domain parts (after trimming).

### Corrected code

See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

- Non-string entries (e.g., `None`, numbers) should be ignored without errors.
- Inputs with multiple `@`, missing local part, or missing domain part should be rejected.
- Whitespace-trimmed valid emails should be accepted; empty list returns `0`.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation

- It claims to safely ignore invalid entries, but the code can crash on non-strings and counts many invalid formats as valid.

### Rewritten explanation

- Iterates over the list and counts only string inputs that contain exactly one `@` with non-empty local and domain parts (after trimming whitespace). Non-string or malformed entries are skipped, and an empty list returns `0`.

## 4) Final Judgment

- Decision: Request Changes
- Justification: The current implementation misclassifies many invalid emails and can fail on non-string inputs.
- Confidence & unknowns: High. Exact email-validity rules are not specified, so validation is a basic heuristic.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings

### Critical bugs

- Uses the total list length as the denominator even though `None` values are skipped, producing an incorrect average.
- Raises `ZeroDivisionError` for empty input or when all values are `None`.
- `float(v)` can raise on non-numeric values, contradicting the "safely handles mixed input types" claim.

### Edge cases & risks

- All values `None` or empty list.
- Non-numeric strings or objects in the list.
- Values like `"nan"` or `"inf"` can propagate non-finite results.

### Code quality / design issues

- Count should reflect only values actually included in the average.
- No explicit handling for invalid/non-convertible values.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Count only values successfully converted to `float`.
- Skip `None` and non-convertible values safely.
- Guard against zero valid values by returning `0`.

### Corrected code

See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

- Empty list and all-`None` list to avoid division by zero.
- Mixed `None` and numeric values to verify correct averaging.
- Numeric strings vs invalid strings/objects to confirm safe skipping.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation

- It claims safe handling of mixed types, but the function raises on non-numeric values.
- It implies an accurate average while using the wrong denominator and risking division by zero.

### Rewritten explanation

- Iterates through the list, skipping `None` and any values that cannot be converted to `float`. It averages only the successfully converted values and returns `0` if none are valid.

## 4) Final Judgment

- Decision: Request Changes
- Justification: The current implementation computes an incorrect average and can crash or mis-handle mixed inputs.
- Confidence & unknowns: High. Returning `0` for no valid values is an assumed policy.
