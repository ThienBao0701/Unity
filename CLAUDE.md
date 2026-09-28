# Unity Exam Starter — Trần Thiên Bảo

## Project Identity
- Student: Trần Thiên Bảo
- Student ID: 23632721
- Course: Công nghệ mới trong phát triển ứng dụng công nghệ thông tin
- Unity version: 2022.3.40f1
- Repository: ThienBao0701/Unity

## Purpose
This is a prepared Unity starter repository for a future university practical exam.
The actual exam question will be provided later and may be completely different from the reference exercises W1-W5.

W1-W5 are reference materials only. They describe the teacher's exercise style, level, and some Unity concepts. They are NOT the predicted exam and must never be treated as the exam specification.

## Repository Structure
- `Assets/Scenes/` — current sample scenes
- `Assets/Scripts/` — current sample scripts
- `Assets/Sprites/` — current sample image assets
- `Packages/manifest.json` — current package dependencies
- `ProjectSettings/ProjectVersion.txt` — Unity version
- `Reference_W1_W5/` — teacher-provided W1-W5 PDFs for reference only
- `EXAM_WORKFLOW.md` — standard future exam workflow
- `CLAUDE_TASK_TEMPLATE.md` — reusable prompt template
- `SCHOOL_PC_SETUP.md` — instructions for opening the project on a school computer

## Current Sample Scenes
- `Assets/Scenes/01_CustomMathDuel.unity` — Math Duel sample
- `Assets/Scenes/02_PlayersInterface.unity` — player interface sample
- `Assets/Scenes/03_ObjectSeparation.unity` — object separation sample

## Current Sample Scripts
- `MathDuelUI.cs` — builds a simple Math Duel UI at runtime
- `ObjectSeparationUI.cs` — demonstrates separated-object cards in a UI
- `SceneBootstrap.cs` — selects which sample UI to attach based on mode

## Current Package/Dependency Notes
The starter is intentionally lightweight. Do not add packages unless the real exam requires them.
The exact dependencies are recorded in `Packages/manifest.json`.

## Important Safety Rules
- Do not delete working files without a reason tied to the actual exam.
- Do not redesign the whole project unnecessarily.
- Do not add speculative gameplay or speculative assets.
- Do not add heavy frameworks when standard Unity components are enough.
- Inspect the existing repository before creating duplicate systems.
- Prefer beginner-friendly, reliable Unity implementations.
- Never claim something was tested unless it was actually tested.
- Clearly report anything that could not be verified.

# EXAM WORKFLOW

1. Read the real exam question carefully.
2. Treat the real exam question as the source of truth.
3. Use W1-W5 only as reference material for style and concepts.
4. Inspect the repository before modifying it.
5. Map every exam requirement to a concrete Unity implementation.
6. Reuse existing assets/scripts when appropriate.
7. Make the minimum changes needed to satisfy the exam.
8. Implement scenes, GameObjects, Components, Scripts, UI, Prefabs, Materials, and Inspector references that are actually required.
9. Avoid unnecessary packages and overengineering.
10. Check C# compilation and obvious broken references.
11. Verify scene setup and Inspector assignments.
12. Verify Play Mode behavior as far as the environment allows.
13. Report every created/modified file.
14. Give clear steps for opening and running the project on the school computer.
15. Explicitly report limitations or unverified items.

## Reference Principle
The files inside `Reference_W1_W5/` are source reference material. They must not be used to invent requirements that are not stated in the real exam.
