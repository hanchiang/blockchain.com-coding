from unittest.mock import patch
from src.config.config import Config
from src.exceptions.exceptions import EnvironmentVariableNotFoundException
import pytest

class TestConfig:
    @patch("os.getenv")
    def test_get_env_var(self, mock_getenv):
        mock_getenv.return_value = "hi"
        
        assert Config.get_env_var("env") == "hi"

    @patch("os.getenv")
    def test_get_env_var_not_found(self, mock_getenv):
        mock_getenv.return_value = None

        with pytest.raises(EnvironmentVariableNotFoundException):
            Config.get_env_var("env")
            
