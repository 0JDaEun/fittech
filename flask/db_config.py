"""Create the database client from deployment-provided settings."""
import os
from supabase import create_client


def _required_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


supabase_url = _required_env("SUPABASE_URL")
supabase_key = _required_env("SUPABASE_KEY")
supabase = create_client(supabase_url, supabase_key)
