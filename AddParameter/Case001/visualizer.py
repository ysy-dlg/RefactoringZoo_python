def visualize_network(model_name, dpi=100):
    print(f"[INFO] Visualizing model: {model_name}")
    print(f"Generating plot with DPI = {dpi}")

    if dpi >= 200:
        print("[DETAIL] High-resolution mode enabled.")
    elif dpi < 80:
        print("[WARNING] DPI too low — image may be blurry.")

# Caller
if __name__ == "__main__":
    visualize_network("resnet50", dpi=150)
