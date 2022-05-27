class LoggerService:

  def info(title, message):
    print(f"\033[32m[{title}]\033[0m {message}")

  def error(title, message):
    print(f"\033[31m[{title}]\033[0m {message}")
  
  def warr(title, message):
    print(f"\033[33m[{title}]\033[0m {message}")

  def log(title, message):
    print(f"[{title}] {message}")