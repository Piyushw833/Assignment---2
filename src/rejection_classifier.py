from typing import Dict, Optional

# Dictionary for mapping rejection reasons
REJECTION_REASONS_MAP = {
    "fake_document": "Fake_document",
    "not_covered": "Not_Covered",
    "policy_expired": "Policy_expired"
}

def handle_error(error_message: str) -> str:
    """Handle errors in rejection classification."""
    print(f"Error: {error_message}")
    return "Error"

def contains_rejection_reason(rejection_text: Optional[str], reason: str) -> bool:
    """Check if rejection text contains a specific reason."""
    try:
        if rejection_text and isinstance(rejection_text, str):
            return reason.lower() in rejection_text.lower()
    except Exception as e:
        handle_error(f"Error in contains_rejection_reason: {str(e)}")
        return False
    return False

def map_rejection_reason(rejection_text: Optional[str]) -> str:
    """Map rejection text to a predefined category."""
    try:
        if rejection_text and isinstance(rejection_text, str):
            for reason, rejection_class in REJECTION_REASONS_MAP.items():
                if contains_rejection_reason(rejection_text, reason):
                    return rejection_class
            return "Unknown"
        else:
            return "No_Remark"
    except Exception as e:
        handle_error(f"Error in map_rejection_reason: {str(e)}")
        return "Error"

def complex_rejection_classifier(remark_text: Optional[str]) -> str:
    """
    Classify rejection remarks into predefined categories.
    
    Fixed bugs:
    1. Changed isinstance check from int to str
    2. Fixed typo in contains_rejection_reasons function name
    3. Added proper null/empty string handling
    4. Fixed return statement typo
    5. Added type hints
    6. Standardized error handling
    """
    try:
        if not isinstance(remark_text, str) or not remark_text or len(remark_text.strip()) == 0:
            return "No_Remark"

        # Check for each rejection reason
        fake_doc = contains_rejection_reason(remark_text, "fake_document")
        not_covered = contains_rejection_reason(remark_text, "not_covered")
        policy_expired = contains_rejection_reason(remark_text, "policy_expired")

        if fake_doc:
            return "Fake_document"
        elif not_covered:
            return "Not_Covered"
        elif policy_expired:
            return "Policy_expired"
        else:
            # Unknown or null remarks
            return map_rejection_reason(remark_text)
    except Exception as e:
        handle_error(f"Error in complex_rejection_classifier: {str(e)}")
        return "Error" 