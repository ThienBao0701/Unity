# CLAUDE.md — Unity Exam Starter (Trần Thiên Bảo, 23632721)

Project memory for future Claude Code sessions. Read this whole file, then `EXAM_WORKFLOW.md`,
before changing anything.

## 0. Rules for every future session

1. **The real exam question is the source of truth.** Nothing else defines the requirements.
2. **W1–W5 are reference examples only.** They show the teacher's style and level. They are not
   the exam and must never be used to invent requirements. The real exam may be completely different.
3. **Inspect the repository before changing anything** (scenes, scripts, `Packages/manifest.json`,
   the Known Issues in §9).
4. **Implement only what the exam requires.** No speculative features, no "nice to have" systems.
5. **Prefer simple, reliable Unity solutions** that a beginner can explain and reproduce in the Editor.
6. **Reuse existing code/assets when appropriate**. Do not build duplicate systems.
7. **Avoid unnecessary packages.** Enable a built-in module or add a package only when a stated
   exam requirement needs it, and report it.
8. **Avoid overengineering**: no frameworks, managers, or architecture the exam does not ask for.
9. **Verify compilation and obvious setup problems** (script/class names, missing modules,
   Inspector references, EventSystem/Camera, Build Settings).
10. **Report exactly what was changed**: every file created, modified or deleted.
11. **Never claim something was tested if it was not actually tested.** A cloud session has no
    Unity Editor (§10). Say clearly what was verified, how, and what the student must still check.
12. Do not delete working files or redesign the project without a reason tied to the real exam.
13. If a problem cannot be fixed safely, document it instead of guessing.

## 1. Project identity

| Item | Value |
|---|---|
| Student | Trần Thiên Bảo |
| Student ID | 23632721 |
| Course | Công nghệ mới trong phát triển ứng dụng công nghệ thông tin (New Technology in IT Application Development) |
| Repository | `ThienBao0701/Unity` (default branch `main`) |
| Unity version | **2022.3.40f1**, changeset `cbdda657d2f0` (from `ProjectSettings/ProjectVersion.txt`) |
| C# language | C# 9 (what Unity 2022.3 compiles) |
| Render pipeline | Built-in (no URP/HDRP package) |

## 2. Repository structure

```
Unity/
├── Assets/
│   ├── Scenes/      01_CustomMathDuel.unity, 02_PlayersInterface.unity, 03_ObjectSeparation.unity (+ .meta)
│   ├── Scripts/     SceneBootstrap.cs, MathDuelUI.cs, ObjectSeparationUI.cs (+ .meta)
│   └── Sprites/     Background.png, SeparatedCharacters.png   (no .meta yet; see §9)
├── Packages/
│   └── manifest.json                 (no packages-lock.json yet; see §9)
├── ProjectSettings/
│   └── ProjectVersion.txt            (the ONLY settings file; see §9)
├── Reference_W1_W5/  W1.pdf … W5.pdf (teacher exercises, reference only)
├── CLAUDE.md                 this file
├── EXAM_WORKFLOW.md          full exam-day workflow + student checklist
├── CLAUDE_TASK_TEMPLATE.md   prompt to paste together with the real exam question
├── SCHOOL_PC_SETUP.md        opening/running the project on a school computer
├── README.md                 short project summary
├── README.txt                legacy note from the W2 homework ZIP (see §12)
└── .gitignore                Unity ignores (Library/, Temp/, Obj/, Build/, Logs/, UserSettings/, .vs/, *.csproj, *.sln, *.apk, *.aab, …)
```

There are no prefabs, materials, animations, audio, fonts or TextMeshPro resources in the repository.

## 3. Scenes

Every scene contains **one** GameObject, `SceneBootstrap`, with the `SceneBootstrap` component. It has
**no Camera, no Light and no EventSystem**. All UI is created by code when Play starts. The `.unity`
files are minimal hand-written YAML (no RenderSettings/Lightmap/SceneRoots blocks). Unity fills in
defaults and rewrites the file the first time the scene is saved in the Editor.

| Scene | `SceneBootstrap.mode` | What happens at Play | Origin |
|---|---|---|---|
| `01_CustomMathDuel.unity` | `CustomInterface` (0) | Adds `MathDuelUI` and builds the Math Duel screen | W2 Task 1/2 (Fig1-inspired, simplified) |
| `02_PlayersInterface.unity` | `PlayersInterface` (1) | **Same as scene 01.** `SceneBootstrap` has no branch for this mode, so it also adds `MathDuelUI`. There is no Fig2 two-player mirrored layout. | W2 Task 2 (not really implemented) |
| `03_ObjectSeparation.unity` | `ObjectSeparation` (2) | Adds `ObjectSeparationUI`: white background, titles, three coloured placeholder "cards" | W2 Task 3 (placeholder only; does not use the PNGs) |

No scene is in Build Settings, because `EditorBuildSettings.asset` does not exist yet.

## 4. Scripts (`Assets/Scripts/`)

| Script | Purpose | Notes |
|---|---|---|
| `SceneBootstrap.cs` | In `Awake`, adds `ObjectSeparationUI` if `mode == ObjectSeparation`, otherwise `MathDuelUI`. | `enum Mode { CustomInterface, PlayersInterface, ObjectSeparation }`. GUID `7d5d6f5b0a4a4f9d9e1c000000000001` is referenced by all 3 scenes. Do not change it. |
| `MathDuelUI.cs` | Builds a Screen-Space-Overlay Canvas (CanvasScaler 1080×1920): title, 2 player score panels, question `a + b = ?`, 30 s timer, 4 answer buttons, Start button "BẮT ĐẦU", and a status line. | Answer buttons have **fixed** labels 18/20/22/24 while the question is random, so a correct answer is rare. Correct gives P1 +10; wrong gives P2 +5. There is no real two-player input. Answers are still accepted after "Hết giờ!". It uses `GameObject.Find` for panels and Vietnamese strings (needs font glyphs). |
| `ObjectSeparationUI.cs` | Builds a white Canvas with the title "TASK 3 – OBJECT SEPARATION" and three coloured `Image` cards labelled OBJECT 01–03. | Static display only. No interaction. |

All UI text uses TextMeshPro (`TextMeshProUGUI`). UI uses `UnityEngine.UI` (`Image`, `Button`, `CanvasScaler`, `GraphicRaycaster`).

## 5. Assets

| Asset | Details | Used by |
|---|---|---|
| `Assets/Sprites/Background.png` | 1080×1920 RGB, pink gradient with circles (Math Duel background) | Nothing yet |
| `Assets/Sprites/SeparatedCharacters.png` | 900×400 RGBA, three figures (red/blue/yellow) on a **transparent** background (≈67 % of pixels alpha 0). One sheet, not yet sliced. | Nothing yet |

In a 3D-mode project these PNGs import as **Texture Type = Default**. To use one in a UI `Image` or a
`SpriteRenderer`, set **Texture Type = Sprite (2D and UI)** and click Apply. Slicing the sheet into
three sprites needs Sprite Mode = Multiple **and** the Sprite Editor, which requires the
`com.unity.2d.sprite` package. That package is not installed (§6).

## 6. Packages / dependencies (`Packages/manifest.json`)

```jsonc
"com.unity.ugui": "1.0.0",                 // UI (Canvas, Image, Button…)
"com.unity.modules.ui": "1.0.0",
"com.unity.textmeshpro": "3.0.6",          // TextMeshPro (was a wrong id, fixed on 2026-09-28)
"com.unity.modules.imgui": "1.0.0",
"com.unity.modules.audio": "1.0.0",        // AudioSource
"com.unity.modules.physics2d": "1.0.0",    // Rigidbody2D, Collider2D
"com.unity.modules.jsonserialize": "1.0.0",// JsonUtility
"com.unity.modules.unitywebrequest": "1.0.0"
```

**This manifest is much smaller than a normal new Unity project.** Everything else is disabled, including:

| If the exam needs… | Enable (Package Manager → Packages: Built-in → select → Enable, or add `"<id>": "1.0.0"` to manifest.json) |
|---|---|
| 3D physics: `Rigidbody`, `BoxCollider`/`SphereCollider`/`CapsuleCollider`, `CharacterController`, `OnCollisionEnter`, `OnTriggerEnter`, `Physics.Raycast` | `com.unity.modules.physics` |
| `Animator`, `Animation`, animation clips | `com.unity.modules.animation` |
| `NavMeshAgent` / NavMesh | `com.unity.modules.ai` |
| `ParticleSystem` | `com.unity.modules.particlesystem` |
| `Texture2D.LoadImage` / `EncodeToPNG` | `com.unity.modules.imageconversion` |
| `VideoPlayer` | `com.unity.modules.video` |
| Terrain | `com.unity.modules.terrain` (+ `com.unity.modules.terrainphysics`) |
| Tilemap | `com.unity.modules.tilemap` |
| UI Toolkit (UIElements) | `com.unity.modules.uielements` |

Without the matching module, the components are missing from **Add Component**, and scripts that use
them fail to compile (`CS0246: type or namespace ... could not be found`).

Registry packages that are **not** installed (install through Package Manager → Unity Registry, which
picks the version verified for 2022.3; only when needed):
- `com.unity.ide.visualstudio`: Visual Studio integration and IntelliSense. It is recommended on a school PC that uses Visual Studio, but it is not in the manifest.
- `com.unity.2d.sprite`: the Sprite Editor (slicing sprite sheets).
- `com.unity.ai.navigation`: NavMesh baking components.
- `com.unity.xr.arfoundation` + a provider (ARCore/ARKit), plus the Android/iOS Build Support modules in Unity Hub: AR. These are heavy, so add them only if the exam explicitly requires AR.
- `com.unity.inputsystem`: **not needed** for keyboard/mouse. The legacy Input Manager (`Input.GetAxis("Horizontal")`, `Input.GetKey`) is the default for regenerated settings. `Horizontal`/`Vertical` already cover WASD and the arrow keys.

## 7. How to open, run, build, test

- **Open:** Unity Hub → Add → *Add project from disk* → select the folder that contains `Assets/`,
  `Packages/`, `ProjectSettings/` → open with **2022.3.40f1**. First open needs internet unless
  TextMeshPro 3.0.6 is already in the machine's package cache. Details are in `SCHOOL_PC_SETUP.md`.
- **First open, once per machine/clone:** check the Console; import TMP Essentials when asked; commit
  the files Unity generates (§9 items 1–3).
- **Run:** open a scene in `Assets/Scenes/` → Play. Scenes 01/02 are identical; 03 is the placeholder.
- **Build:** File → Build Settings → *Add Open Scenes* (the list is empty) → choose platform → Build.
  Build into a `Build/` or `Builds/` folder (git-ignored).
- **Test:** there are no automated tests and no Test Framework package. Testing means Console with 0
  errors plus manual Play Mode checks in the Editor.

## 8. Coding conventions

- One `MonoBehaviour` per file; **file name = class name** (otherwise Unity cannot attach it).
- Folders: scripts → `Assets/Scripts/`, scenes → `Assets/Scenes/`, and create `Assets/Materials/`,
  `Assets/Prefabs/` etc. only when needed. W4 shows materials in `Assets/Materials`.
- Match the level of the existing code: plain `MonoBehaviour`s, `Start`/`Update`, no extra frameworks.
- Prefer objects built **in the Editor** (visible in the Hierarchy and wired in the Inspector) unless
  the exam says otherwise. The existing samples build UI from code; that works, but it is harder to
  show and grade. Reuse them only where the exam fits.
- Inspector references: `public` or `[SerializeField] private` fields, named clearly; tell the
  student exactly what to drag where.
- UI text: TextMeshPro (`TMP_Text`/`TextMeshProUGUI`); it is already a dependency. Every UI scene
  needs an **EventSystem** for clicks.
- Input: legacy Input Manager unless the exam demands the new Input System.
- Save `.cs` files as UTF-8 (Vietnamese text is used). Check that the font has the glyphs.
- Do not hand-edit `.unity`/`.prefab` YAML beyond trivial changes; prefer Editor steps for the student.
- Never change existing `.meta` GUIDs; scenes reference scripts by GUID.

## 9. Known issues (state on 2026-09-28)

**Fixed during preparation** (commit "Fix blockers that stop the starter project from opening and compiling"):
- `Packages/manifest.json` listed `com.unity.modules.textmeshpro`, which does not exist, so package
  resolution would fail and UGUI/TMP would not load. It is now `com.unity.textmeshpro` 3.0.6.
- `MathDuelUI.cs` lines 77–80 passed a `Color` as the button `size` (4× `CS1503`). A compile error
  blocks Play Mode for the **whole project**. It now passes `new Vector2(420,130)`; positions and
  colours are unchanged.
- Scene `.meta` files had malformed 21-character GUIDs (Unity needs 32 hex characters). They now
  have valid GUIDs and the standard `DefaultImporter` block.
- `ProjectVersion.txt` had a wrong changeset (`9e2d8a7f7f3e`). It is now `cbdda657d2f0`, the real
  2022.3.40f1 changeset, so Unity Hub can install the exact editor.
- `.gitignore` now also ignores `.vs/`, `*.apk`, `*.aab`.

**Still open (documented, not changed):**
1. `ProjectSettings/` has only `ProjectVersion.txt`. Unity regenerates every other settings file
   with defaults on first open: 3D mode, legacy Input Manager, empty Build Settings scene list, and
   default Player settings. After the first successful open, **commit `ProjectSettings/*.asset`**
   so every computer shares the same settings.
2. There are no `.meta` files for the folders or the two PNGs, and no `Packages/packages-lock.json`.
   Unity generates them. **Commit them after the first open**, otherwise each computer creates
   different GUIDs and references to those assets break between machines.
3. TMP Essential Resources are not in the repo. The first time TMP text is created, Unity shows the
   *TMP Importer* window. Click **Import TMP Essentials** (or Window → TextMeshPro → Import TMP
   Essential Resources). This creates `Assets/TextMesh Pro/`; commit it. Text is invisible until then.
4. No **EventSystem** in any scene, so the sample buttons will not react to clicks. If needed:
   GameObject → UI → Event System, then save the scene.
5. No **Camera** in any scene. The Game view shows "No cameras rendering", though the overlay UI still draws.
6. Scene 02 is a duplicate of scene 01 at runtime (see §3).
7. Most built-in modules are disabled and there is no IDE package (see §6).
8. Vietnamese diacritics (e.g. "BẮT ĐẦU") may render as □ if the default TMP font lacks the
   glyphs. **Unverified.**
9. The PNGs are unused and import as Default textures (§5).
10. Whether 2022.3.40f1 installs TextMeshPro 3.0.6 offline is **unverified**. Open the project with
    internet the first time.

## 10. What a cloud session can and cannot verify

- There is **no Unity Editor** in the cloud container. During preparation the network also blocked
  `packages.unity.com` and `unity.com`. Package resolution, asset import, scene loading, Play Mode, visuals and builds
  **cannot** be verified there. The student must check them in Unity.
- What *can* be checked: JSON validity of `manifest.json`, `.meta` GUID format (32 hex characters),
  file/class name matches, GUID references between scenes and scripts, and C# syntax and semantics.
- During preparation, the scripts were compiled with Roslyn (C# 9) against hand-written stubs of the
  Unity/UGUI/TMP APIs they use. The runtime and compiler came from NuGet/PyPI into the session
  scratchpad; none of it is committed. This proves the C# is valid **for the stubbed API only**. It is
  not a Unity compile. Report such checks with that caveat.

## 11. Important warnings

- **Open only with 2022.3.40f1** (another 2022.3.x patch is usually fine: Hub → "Change version" →
  Continue). **Do not open with Unity 6 or 2023.x.** That upgrades the project (TMP merges into
  UGUI 2.0) and it may not reopen cleanly in 2022.3.
- Do not commit `Library/`, `Temp/`, `Logs/`, `UserSettings/`, `.vs/`, `*.csproj`, `*.sln`, builds.
- Do not rename/move assets outside Unity (the `.meta` must move with the asset).
- Keep the project path short and ASCII-only (e.g. `C:\Unity\Exam23632721`), not in OneDrive.
- `README.txt` is the old W2 homework note. Its "2022.3 LTS or newer" line is superseded by the rule above.

## 12. W1–W5: reference material only

`Reference_W1_W5/*.pdf` are the teacher's weekly exercises (course "New Technology in IT Application
Development"; W5 is signed by Nguyen Ngoc Le). **They are reference examples, not the exam.** Use them
only to understand the expected level, style, and common Unity concepts. **Never use them to invent
exam requirements, and do not assume the exam reuses their scenes, scripts, gameplay, or assets.**

| Week | Content (summary) | Unity concepts it touches |
|---|---|---|
| W1 | Two 3D scene designs: a blue floor with white walls and a yellow ball; a room with inner walls, a capsule player with the camera on top of it, directional + point lights | Primitives, Transform, materials, lights, camera placement |
| W2 | Math Duel UI (Fig1: portrait mobile menu in Vietnamese); Fig2: face-to-face two-player layout; choose Fig1 or Fig2 for a custom interface; separate objects in an image and remove background (minifigures, droid pictures) | Canvas/UI layout, buttons, text, sprites/transparency. **This repo's current scenes come from W2.** |
| W3 | Design a 3D robot (R2-D2-like, "Beni" robot); install NVIDIA Isaac Sim (Windows/Linux); design a robot arm/hand in Unity and open it in Isaac Sim | 3D modelling with primitives, hierarchies, external tools |
| W4 | "Design, build and run": ball-and-wall collision changes the wall material and shows "Ouch!" / "Keep Rolling..." (materials after-collision, ball-color, floor-color, wall-color); a robot chasing a character in a maze, with the character controlled by WASD + arrow keys | Physics collisions, materials, UI text, keyboard input, chasing/following, building |
| W5 | AR app: plane detection, bounding box detection, place a 3D object on a touched plane; an interactive game (Fig2 math duel) deployed to a mobile device | AR Foundation, touch input, mobile build |

Note: most W1/W3/W4 concepts need modules that are **not enabled** here (`physics`, `animation`, `ai`, see §6).
Enable them only when the real exam needs them.

## 13. EXAM WORKFLOW

Full version with the student checklist: **`EXAM_WORKFLOW.md`**. Prompt template: **`CLAUDE_TASK_TEMPLATE.md`**.

```
Real Exam Question
→ Analyze every requirement
→ Do NOT assume similarity to W1-W5
→ Inspect current repository
→ Decide what can be reused
→ Plan minimal changes
→ Implement only required features
→ Verify scripts
→ Verify scene setup
→ Verify Inspector references
→ Verify Play Mode
→ Verify build configuration
→ Report changed files
→ Give step-by-step instructions for the student
```
