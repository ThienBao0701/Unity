# Exam guide: open, check, finish, export (Trần Thiên Bảo, 23632721)

Branch: `exam/actual-exam-2d-3d`. Unity **2022.3.40f1** only (never Unity 6 / 2023.x).

## 1. Open

1. Get the branch: `git fetch && git checkout exam/actual-exam-2d-3d`, or on GitHub switch to the branch →
   *Code* → *Download ZIP* → extract to a short ASCII path (e.g. `C:\Unity\Exam23632721`).
2. Unity Hub → *Add project from disk* → select the folder that contains `Assets/`, `Packages/`, `ProjectSettings/`
   → open with 2022.3.40f1 (be online the first time: TextMeshPro 3.0.6 is downloaded).
3. **Console must show 0 red errors.** (If the TMP importer window pops up, click *Import TMP Essentials*;
   the exam scenes don't use text, so it is only for the old sample scenes.)

## 2. Run and check each question

| Scene (Project window) | Press Play and expect |
|---|---|
| `Assets/Exam/2D/Scenes/Cau1_PlanetMove2D` | The globe (no white box, light-blue background) moves slowly **left → right**; after x = 7 it restarts at x = -7. |
| `Assets/Exam/2D/Scenes/Cau2_RocketOrbit2D` | Same planet movement **and** the rocket flies in a circle around the planet (one loop ≈ 8 s), nose pointing along its flight direction. |
| `Assets/Exam/3D/Scenes/Cau3_Robot3D` | Orange robot on a grey floor. The **neck + head turn continuously** by themselves. Click the Game view once, then hold **W** → robot moves forward (toward the camera side, the side with the eyes); hold **S** → it moves back. |

Values to tweak in the Inspector if something looks off: `Planet → PlanetMove2D.moveSpeed`,
`Rocket → RocketOrbit2D.radius / orbitSpeed / spriteNoseAngle`, `Neck → NeckRotate.rotateSpeed`,
`Robot → RobotMovement.moveSpeed`.

## 3. MUST DO: replace the placeholder images with the real exam images (Câu 1a)

The cloud session could **not** download from dreamstime.com (blocked by its network policy), so
`Assets/Exam/2D/Sprites/Planet.png` and `Rocket.png` are **self-drawn placeholders** processed by the
real background-removal script. Replace them:

1. Open both exam links and download the preview images (`rocket.jpg`, `globe.jpg`).
2. Remove the white background. Choose one method:
   - Python: `pip install pillow numpy`, then
     `python Exam_Report/tools/remove_background.py rocket.jpg Rocket.png` (and `globe.jpg Planet.png`).
   - or remove.bg / Photoshop / GIMP (*Colors → Color to Alpha → white*), export as PNG.
   - Open the PNG and check it: if white continents inside the globe also disappeared, redo that one
     with GIMP (Fuzzy Select only the outside white → Delete).
3. **Overwrite** `Assets/Exam/2D/Sprites/Planet.png` and `Rocket.png` (same names; keep the `.meta`
   files, so the scenes keep their references).
4. In Unity, select each PNG: Texture Type must stay **Sprite (2D and UI)**. Set **Pixels Per Unit** ≈
   `image width in px ÷ 2.6` for Planet and `÷ 1.5` for Rocket → *Apply*.
5. Open `Cau2_RocketOrbit2D`, select `Rocket`, set `spriteNoseAngle` to the direction the rocket nose
   points in the picture (0 = right, 45 = up-right, 90 = up, 135 = up-left). Play and check the nose follows the circle.
6. Put the original and processed images in the report.

## 4. Save and commit the files Unity generates

After the first successful open: File → Save Project, then commit `ProjectSettings/*.asset`,
`Packages/packages-lock.json`, and any new `.meta` files (see `CLAUDE.md` §9).

## 5. Screenshots for the report

Game view (maximise with *Play Maximized* or Shift+Space): 2–3 frames of each 2D scene, the robot from
the front, the head turned, and the robot before/after W and S. Scene view + Hierarchy of the robot.
Insert them where `BaoCao_23632721_TranThienBao.md` says `[CHÈN ẢNH]`.

## 6. Export the two packages (Assets → Export Package)

**2D package**
1. Project window → select folder `Assets/Exam/2D`.
2. Menu **Assets → Export Package...**
3. Check that everything under `Exam/2D` is ticked (Scenes, Scripts, Sprites). Keep *Include dependencies* ticked.
4. *Export...* → name it `23632721_TranThienBao_2D.unitypackage`.

**3D package**
1. Select folder `Assets/Exam/3D`.
2. **Assets → Export Package...** → Scenes, Scripts, Materials ticked → *Export...* →
   `23632721_TranThienBao_3D.unitypackage`.

Test (optional): create a new empty 2022.3 3D project → Assets → Import Package → Custom Package → the
file → open the scene → Play.
