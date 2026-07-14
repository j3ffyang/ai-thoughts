# Linux System Customization: Enabling URI Link Handlers for AppImages (Wayland/Hyprland)

This guide documents how to manually register custom URI protocols (e.g., `obsidian://`, `tg://`, `zoommtg://`) for standalone **AppImage** applications on minimalist Linux environments like Arch Linux running Hyprland.

---

## The Problem
Minimalist window managers lack desktop environment automation (like GNOME or KDE). When clicking a protocol link in a web browser (e.g., Firefox), the system fails to forward the link because:
1. No `.desktop` configuration file exists for the standalone AppImage binary.
2. The browser or `xdg-open` doesn't know which application owns the custom protocol scheme.
3. Standard path shortcuts like the tilde (`~`) are rejected by XDG standards inside system files.

---

## Step-by-Step Solution

### Step 1: Install MIME-Type Parsing Tools
Ensure your system has the tools required to map application associations without a heavy desktop environment.
```bash
sudo pacman -S xdg-utils perl-file-mimeinfo
```

### Step 2: Create a Custom System Entry
You must manually write an XDG-compliant `.desktop` configuration file so your system recognizes the application.

1. Create the application entry file:
   ```bash
   nano ~/.local/share/applications/obsidian.desktop
   ```
2. Paste the configuration block below.
   * **CRITICAL:** You **must** use the absolute file path (e.g., `/home/username/...`). Do not use `~`.
   * Include the `%U` variable at the end of the `Exec` line to pass the browser URI data directly to the binary.

```ini
[Desktop Entry]
Name=Obsidian
Comment=Markdown Notetaking App
Terminal=false
Type=Application
Icon=obsidian
Exec=/home/jeff/pool/Downloads/rog_drive/Obsidian-gen.AppImage --ozone-platform-hint=auto %U
MimeType=x-scheme-handler/obsidian;
Categories=Office;TextEditor;
```
*(Note: `--ozone-platform-hint=auto` ensures the application runs natively on Wayland under Hyprland).*

### Step 3: Make the AppImage Executable
Verify that your user account has direct execution permissions for the application binary:
```bash
chmod +x /home/jeff/pool/Downloads/rog_drive/Obsidian-gen.AppImage
```

### Step 4: Rebuild the Desktop Database and Bind Protocol
Force the XDG system to index your new file and explicitly bind the URI scheme (`x-scheme-handler/obsidian`) to the application metadata.

```bash
# Update local index cache
update-desktop-database ~/.local/share/applications/

# Bind the handler protocol directly to your custom desktop file
xdg-mime default obsidian.desktop x-scheme-handler/obsidian
```

---

## Verification & Testing

### 1. Terminal Check
Run a test command via your terminal to ensure `xdg-open` bypasses generic fallbacks (like crashing on `x-www-browser`) and launches your app directly:
```bash
xdg-open "obsidian://open"
```
*If successful, your AppImage window will instantly open.*

### 2. Browser Check
1. Fully **close and restart** Firefox to flush its internal protocol handler cache.
2. Click the browser/clipper link again.
3. When prompted by Firefox, select **Obsidian**, check **"Always allow"**, and click **Open Link**.
