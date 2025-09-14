"""
Dependency injection container for Pulsepipe core services.

This module defines the `bootstrap_container()` function, which initializes
a Wired ServiceRegistry and registers all core services, including:

- Config (singleton)
- PageStore

Each service is registered with appropriate lifecycle management and can be
resolved via `container.get(ServiceClass)` in CLI, API, or test contexts.

Usage:
    from pulsepipe.core.container import bootstrap_container

    container = bootstrap_container()
    page_st = container.get(PageStore)
"""

from wired import ServiceRegistry
from pulsepipe.core.config import Config
from pulsepipe.storage.pagestore import PageStore

def bootstrap_container() -> ServiceRegistry:
    """
    Bootstraps the dependency injection container with core services.
    
    Returns:
        ServiceRegistry: The configured service registry.
    """

    registry = ServiceRegistry()

    # Register Config as singleton
    config = Config.load()
    registry.register_singleton(config, Config)

    # Register services with factories
    registry.register_factory(lambda container: PageStore(container.get(Config)), PageStore)

    return registry
