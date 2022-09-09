from unittest.mock import patch
from src.exceptions.exceptions import DependencyNotFoundException
import pytest
from src.dependencies.dependencies import Dependencies
from src.service.blockchain_order_book_service import BlockChainOrderBookService
from src.transformer.blockchain_order_book_transformer import BlockChainOrderBookTransformer
from src.dao.metadata_memory_dao import MetadataMemoryDao
from src.service.csv_metadata_parser import CsvMetadataParser

class TestConfig:
    @patch("src.dependencies.dependencies.Config.get_env_var")
    def test_get_order_book_service(self, mock_config):

        mock_config.return_value = "url"
        
        Dependencies.build()
        blockchain_order_book_service = Dependencies.get_order_book_service("blockchain.com")
        assert isinstance(blockchain_order_book_service, BlockChainOrderBookService)
            
    @patch("src.dependencies.dependencies.Config.get_env_var")
    def test_get_order_book_service_not_found(self, mock_config):
        mock_config.return_value = "url"
        
        Dependencies.build()

        with pytest.raises(DependencyNotFoundException):
            Dependencies.get_order_book_service("random")

    @patch("src.dependencies.dependencies.Config.get_env_var")
    def test_get_order_book_transformer(self, mock_config):
        mock_config.return_value = "url"
        Dependencies.build()
        blockchain_order_book_transformer = Dependencies.get_order_book_transformer("blockchain.com")
        
        assert isinstance(blockchain_order_book_transformer, BlockChainOrderBookTransformer)

    @patch("src.dependencies.dependencies.Config.get_env_var")
    def test_get_order_book_transformer_not_found(self, mock_config):
        mock_config.return_value = "url"
        Dependencies.build()
        
        with pytest.raises(DependencyNotFoundException):
            Dependencies.get_order_book_transformer("random")

    @patch("src.dependencies.dependencies.Config.get_env_var")
    def test_get_metadata_dao(self, mock_config):
        mock_config.return_value = "url"
        Dependencies.build()
        metadata_dao = Dependencies.get_metadata_dao("memory")

        assert isinstance(metadata_dao, MetadataMemoryDao)

    @patch("src.dependencies.dependencies.Config.get_env_var")
    def test_get_metadata_dao_not_found(self, mock_config):
        mock_config.return_value = "url"
        Dependencies.build()

        with pytest.raises(DependencyNotFoundException):
            Dependencies.get_metadata_dao("random")

    @patch("src.dependencies.dependencies.Config.get_env_var")
    def test_get_metadata_parser(self, mock_config):
        mock_config.return_value = "url"
        Dependencies.build()
        metadata_parser = Dependencies.get_metadata_parser("csv")

        assert isinstance(metadata_parser, CsvMetadataParser)
    
    @patch("src.dependencies.dependencies.Config.get_env_var")
    def test_get_metadata_parser_not_found(self, mock_config):
        mock_config.return_value = "url"
        Dependencies.build()

        with pytest.raises(DependencyNotFoundException):
            Dependencies.get_metadata_parser("random")
