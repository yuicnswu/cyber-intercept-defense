import random

def inject_zero_width_spaces(text):
    """
    Injects Zero-Width Non-Joiners (ZWNJ - \u200C) randomly between Thai characters.
    This breaks simple string matching (like regex) without changing how it looks to the user.
    """
    zwnj = '\u200C'
    result = ""
    for char in text:
        result += char
        # 30% chance to insert an invisible space after a character
        if random.random() < 0.3:
            result += zwnj
    return result

def apply_thai_homoglyphs(text):
    """
    Swaps characters for visually similar ones (Homoglyphs).
    e.g., Thai zero (๐) for English zero (0), or B for Baht (฿).
    """
    homoglyphs = {
        '0': '๐', # English 0 to Thai 0
        'O': '0', # Letter O to Zero
        'เ': 'e', # Sara E to English e (sometimes used in visual spoofing)
        'B': '฿', # English B to Baht symbol
        'โอน': 'โ0น', # Specific trigger word obfuscation
        'บัญชี': 'บํญชี' # Intentional common typo
    }
    
    result = text
    for key, value in homoglyphs.items():
        if key in result:
            # 50% chance to replace to create variance in the dataset
            if random.random() < 0.5:
                result = result.replace(key, value)
    return result

def obfuscate_spacing(text):
    """
    Randomly inserts spaces inside sensitive trigger words.
    """
    trigger_words = ["โอนเงิน", "อายัด", "ตำรวจ", "บัญชีม้า"]
    result = text
    for word in trigger_words:
        if word in result:
            # Insert a space in the middle of the word: โอนเงิน -> โอน เงิน
            split_idx = len(word) // 2
            obfuscated = word[:split_idx] + " " + word[split_idx:]
            result = result.replace(word, obfuscated)
    return result

def generate_evasion_sample(original_text):
    """Applies a random combination of adversarial evasion techniques."""
    text = original_text
    
    if random.random() < 0.7:
        text = obfuscate_spacing(text)
    if random.random() < 0.7:
        text = apply_thai_homoglyphs(text)
    if random.random() < 0.5:
        text = inject_zero_width_spaces(text)
        
    return text

# --- Example Usage for your Ph.D. Dataset ---
if __name__ == "__main__":
    baseline_scam_texts = [
        "บัญชีของคุณถูกอายัด กรุณาโอนเงินเพื่อตรวจสอบ",
        "พัสดุของคุณตกค้าง กรุณากดลิงก์เพื่อชำระค่าปรับ",
        "คุณได้รับสินเชื่อ 50,000B กรุณาโอนเงินมัดจำก่อน"
    ]
    
    print("=== Adversarial Thai Evasion Generator ===\n")
    for original in baseline_scam_texts:
        print(f"Original (Baseline): {original}")
        print(f"Evasion (Perturbed): {generate_evasion_sample(original)}")
        print("-" * 40)
