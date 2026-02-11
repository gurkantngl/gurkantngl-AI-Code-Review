# Notes (Optional)

Assumptions / limitations kept intentionally minimal:
- When there are no valid items (all cancelled orders, empty list, all None), the functions return 0 instead of raising an error.
- Email validation is a basic heuristic: exactly one "@" with non-empty local and domain parts after trimming; it does not attempt full RFC validation.
- For measurements, non-convertible values are skipped; non-finite floats ("nan", "inf") are not explicitly filtered.
- Inputs are assumed to match the expected structure (e.g., orders contain "status" and "amount"); missing keys are not handled to keep fixes minimal.