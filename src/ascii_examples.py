from art import text2art, FONT_NAMES

def preview_fonts(text="Crawler"):
    for font in FONT_NAMES:
        print(f"\n=== Font: {font} ===")
        try:
            print(text2art(text, font=font))
        except Exception as e:
            print(f"[Error rendering font '{font}']: {e}")

if __name__ == "__main__":
    preview_fonts()