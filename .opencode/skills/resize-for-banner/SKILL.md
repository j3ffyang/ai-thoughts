---
name: resize-for-banner
description: >
  Rescale an image (usually a screenshot from imgs/) into social banner
  versions: 16:9 for the LinkedIn article header and 5:2 for Twitter/X, using
  ImageMagick. The image is resized to fit and the leftover space is padded
  black — never cropped. Use when the user wants a banner, cover photo, or
  "16:9 / 5:2" version for a social profile or article header. Never
  overwrites the original — creates new files beside it.
---

# Resize for Banner (LinkedIn / Twitter)

Turn one image into social banner variants with ImageMagick, keeping the original file untouched and writing new files beside it. The image is **rescaled to fit and black-padded**, never cropped, so no content is lost.

## Platform specs

- **LinkedIn article** — 16:9 ratio, 1200x675 px (article header image).
- **Twitter / X** — 5:2 ratio, 1500x600 px (header photo).
- If two requested ratios are identical there is no reason to make both; otherwise produce one per distinct size.
- 16:9 and 5:2 differ, so normally **two** files are produced.

## Approval gate

- **Never touch the original image.** All output goes to new files named after the original (suffix added, base name unchanged).
- Confirm the plan with the user before converting: the source image, the target size(s), and the exact output filenames.
- If the user asks for a size the spec does not cover (e.g. 1500x600 / 5:2), use that size with the same resize + pad technique and say which platform it suits.

## Inputs

- `source` — Path to the original image, e.g. `ai-thoughts/imgs/260806-1656.png`. Required.
- `sizes` — Which banners to produce. Default: LinkedIn article 1200x675 and Twitter 1500x600.

## Outputs

- `imgs/<base>-banner-linkedin.png` — 1200x675 (16:9 article), aspect preserved, black padding.
- `imgs/<base>-banner-twitter.png` — 1500x600 (5:2), aspect preserved, black padding.
- `<base>` keeps the original filename exactly (e.g. `260806-1656` → `260806-1656-banner-linkedin.png`). The original file is never modified.

## Procedure

1. **Confirm the plan** with the user: source image, target sizes, output filenames. Get a go-ahead before writing files.
2. **Check the original dimensions** with `identify` or `magick identify "<source>"` so you can predict which axis will be padded.
3. **Resize to fit, then pad with black** with ImageMagick 7 `magick`:

   ```sh
   # LinkedIn article — fit inside 1200x675, center on black 1200x675 canvas
   magick <source> -resize "1200x675" -background black -gravity center \
     -extent 1200x675 imgs/<base>-banner-linkedin.png

   # Twitter — fit inside 1500x600, center on black 1500x600 canvas
   magick <source> -resize "1500x600" -background black -gravity center \
     -extent 1500x600 imgs/<base>-banner-twitter.png
   ```

   - `-resize "WxH"` (no bang) scales to fit inside the box, preserving the
     aspect ratio — the image is never distorted or cropped.
   - `-extent WxH` then pads the leftover space; `-background black` makes the
     padding dark and `-gravity center` centers the image.
   - If the source is taller/narrower than the target ratio, padding appears on
     the left and right; if it is wider, padding appears on top and bottom.
   - Padding color is black by default; ask the user if they want a different
     background.
4. **Verify** every output with `identify` — dimensions must match the target size exactly.
5. **Report** the output paths and confirm the original is untouched (git status shows the new files as untracked, the original unmodified).

## Quality rules

- Never overwrite or rename the source image.
- **Never crop the image.** Resize to fit and pad — cropping loses content.
- Do not invent dimensions: LinkedIn article = 1200x675, Twitter = 1500x600.

## Verification

- `identify` reports exactly 1200x675 and 1500x600 for the two outputs.
- The source image inside the banner is undistorted (aspect ratio preserved).
- The original file is byte-identical (unchanged `identify` output / git status).
- Output files sit beside the original in the same directory.

## Error Handling

- **Source not found**: list candidate images in `imgs/` and ask which to use.
- **Output already exists**: stop and ask whether to overwrite, or choose a different suffix.
- **User wants one image for both platforms**: explain that 16:9 and 5:2 differ, so a single image cannot satisfy both exact specs; offer to make both, or a single compromise size if the user insists.
- **No ImageMagick**: `magick` is always installed on the user's machines — skip checking for it and run the commands directly.
