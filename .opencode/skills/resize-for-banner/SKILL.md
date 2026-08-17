---
name: resize-for-banner
description: >
  Rescale an image into social banner versions using ImageMagick. The image is
  resized to fit and the leftover space is padded black — never cropped. Use when
  the user wants a banner, cover photo, or resized version for a social profile
  or article header. Never overwrites the original — creates new files beside it.
  Defaults to Twitter/X (5:2, 1500x600); other platforms available on request.
---

# Resize for Banner

Turn one image into social banner variants with ImageMagick, keeping the original file untouched and writing new files beside it. The image is **rescaled to fit and black-padded**, never cropped, so no content is lost.

## Platform specs

| Platform | Ratio | Dimensions | Notes |
|----------|-------|------------|-------|
| Twitter / X | 5:2 | 1500x600 | Header photo. **Default.** |
| LinkedIn article | 16:9 | 1200x675 | Article header. Usually unnecessary — generated infographics are already 16:9. |
| YouTube channel | 16:9 | 2560x1440 | Channel art; safe area is 1546x423 center. |
| Blog / generic | any | any WxH | Custom dimensions on request. |

If the user does not specify a platform, default to Twitter (1500x600).

## Approval gate

- **Never touch the original image.** All output goes to new files named after the original (suffix added, base name unchanged).
- Confirm the plan with the user before converting: the source image, the target size(s), and the exact output filenames.
- If the user asks for a size the spec does not cover, use that size with the same resize + pad technique and say which platform it suits.

## Inputs

- `source` — Path to the original image, e.g. `ai-thoughts/imgs/260806-1656.png`. Required.
- `sizes` — Which banners to produce. Default: Twitter 1500x600. User may request any platform from the specs table or custom dimensions.

## Outputs

- `imgs/<base>-banner-<platform>.png` — e.g. `260806-1656-banner-twitter.png`.
- `<base>` keeps the original filename exactly. The original file is never modified.

## Procedure

1. **Confirm the plan** with the user: source image, target size(s), output filename(s). Get a go-ahead before writing files.
2. **Check the original dimensions** with `magick identify "<source>"` so you can predict which axis will be padded.
3. **Resize to fit, then pad with black** with ImageMagick 7 `magick`:

   ```sh
   magick <source> -resize "<W>x<H>" -background black -gravity center \
     -extent <W>x<H> imgs/<base>-banner-<platform>.png
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
- Do not invent dimensions. Use the platform specs table or the user's explicit dimensions.

## Verification

- `identify` reports exactly the target dimensions for each output.
- The source image inside the banner is undistorted (aspect ratio preserved).
- The original file is byte-identical (unchanged `identify` output / git status).
- Output files sit beside the original in the same directory.

## Error Handling

- **Source not found**: list candidate images in `imgs/` and ask which to use.
- **Output already exists**: stop and ask whether to overwrite, or choose a different suffix.
- **No ImageMagick**: `magick` is always installed on the user's machines — skip checking for it and run the commands directly.
