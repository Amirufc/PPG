import secrets
import string

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_special=True, 
                      min_upper=2, min_lower=2, min_digits=2, min_special=2, custom_special="!@#$%"):
    # بررسی سریع ورودی‌ها
    if length < 14 or not isinstance(length, int):
        return None, "Invalid length: must be an integer >= 14"
    
    # تعریف مجموعه کاراکترها با حذف مبهم‌ها
    ambiguous = "Il1O0"
    upper = ''.join(c for c in string.ascii_uppercase if c not in ambiguous) if use_upper else ""
    lower = ''.join(c for c in string.ascii_lowercase if c not in ambiguous) if use_lower else ""
    digits = ''.join(c for c in string.digits if c not in ambiguous) if use_digits else ""
    special = ''.join(c for c in custom_special if c not in ambiguous) if use_special else ""
    chars = upper + lower + digits + special

    # بررسی حداقل‌ها و فعال بودن نوع کاراکتر
    total_min = (min_upper if use_upper else 0) + (min_lower if use_lower else 0) + \
                (min_digits if use_digits else 0) + (min_special if use_special else 0)
    if total_min > length or not chars:
        return None, "Invalid configuration: minimums exceed length or no characters enabled"

    # تولید مستقیم رشته
    password = ""
    if use_upper:
        password += ''.join(secrets.choice(upper) for _ in range(min_upper))
    if use_lower:
        password += ''.join(secrets.choice(lower) for _ in range(min_lower))
    if use_digits:
        password += ''.join(secrets.choice(digits) for _ in range(min_digits))
    if use_special:
        password += ''.join(secrets.choice(special) for _ in range(min_special))
    
    # پر کردن بقیه
    password += ''.join(secrets.choice(chars) for _ in range(length - len(password)))

    # تبدیل به لیست برای مخلوط کردن و برگردوندن به رشته
    pwd_list = list(password)
    secrets.SystemRandom().shuffle(pwd_list)
    return ''.join(pwd_list), "Success"

# تست‌ها
if __name__ == "__main__":
    print("Only lowercase and numbers:", *generate_password(32, use_upper=False, use_special=False))
    print("All types:", *generate_password(32))
    print("Only numbers:", *generate_password(32, use_upper=False, use_lower=False, use_special=False))
    print("No special:", *generate_password(32, use_special=False))