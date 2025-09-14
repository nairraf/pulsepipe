# 🧠 Pulsepipe Developer Journal

A running log of architectural decisions, design experiments, and future ideas for the Pulsepipe assistant stack.

---

## 📅 Architecture Decisions

### [2025-09-13] Dependency Injection
- Adopted **Wired** for unified DI across CLI and API layers.
- Centralized service registration in `core/container.py`.
- FastAPI routes resolve dependencies via adapters in `api/dependencies.py`.

### [2025-09-13] Object-Oriented Core
- All core modules use **service classes** for encapsulation.
- Stateless utilities live as `@staticmethod`s within domain classes.
- Improves testability, DI integration, and future extensibility.

---

## 🧪 Testing Strategy

- Use **Pytest** with `pytest-mock` for mocking external systems.
- Focus tests on `core/` logic first; CLI/API wrappers get smoke tests.
- Snapshot testing planned for creative workflows (e.g. design, palettes).
- Fixtures live in `tests/conftest.py` for reusable setup.

---

## 🚧 TODOs & Technical Debt

- [ ] Add caching layer to `MemoryService` for repeated queries.
- [ ] Refactor `Embedder` to support multiple backends (e.g. Nomic, OpenAI).
- [ ] Implement plugin registration for agent personas.
- [ ] Snapshot test output of `DesignService.generate_palette()`.

---

## 💡 Ideas & Experiments

- `#plugin` Consider dynamic tool routing via agent personas.
- `#fastapi` Explore WebSocket support for streaming responses.
- `#di` Investigate scoped lifecycles in Wired for agent sessions.
- `#testing` Auto-extract TODOs from source via ripgrep or static script.

---

## 🧩 Tag Conventions (for source code)

Use structured comments in `.py` files to track ideas:

```python
# @todo: Refactor into MemoryService
# @idea: Support multiple embedder backends
# @plugin: Persona hook for ingest pipeline
