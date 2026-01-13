
import unittest
from unittest.mock import patch, MagicMock
from src.arxiv_client import fetch_latest_papers, filter_papers_by_keywords
from src.main import main
import src.llm_client
import datetime
import os

class TestPaperCuration(unittest.TestCase):
    
    def test_fetch_and_filter(self):
        """Test arXiv fetching and keyword filtering logic (mocked network)"""
        with patch('src.arxiv_client.arxiv.Client') as mock_client_cls:
            mock_client = MagicMock()
            mock_client_cls.return_value = mock_client
            
            # Mock arXiv result
            mock_result = MagicMock()
            mock_result.title = "Adversarial Attacks on LLMs for Safety"
            mock_result.summary = "We explore safety jailbreaks."
            mock_result.published = datetime.datetime.now(datetime.timezone.utc)
            mock_result.entry_id = "http://arxiv.org/abs/1234.5678"
            
            # Mock results generator
            mock_client.results.return_value = [mock_result]
            
            papers = fetch_latest_papers()
            self.assertEqual(len(papers), 1)
            
            filtered = filter_papers_by_keywords(papers)
            self.assertEqual(len(filtered), 1)
            
    @patch('src.llm_client.genai.Client')
    def test_main_flow(self, mock_client_cls):
        """Test the main orchestrator with mocked LLM"""
        
        # Mock Client instance
        mock_client = MagicMock()
        mock_client_cls.return_value = mock_client
        
        # Mock categorization response
        mock_response = MagicMock()
        mock_response.text = '{"relevant": true, "category": "Robustness & Generalization", "summary": "A great paper.", "explanation": "test"}'
        
        # Mock highlight response
        mock_highlight_response = MagicMock()
        mock_highlight_response.text = "New attacks discovered."
        
        # We need to handle multiple calls to generate_content
        # client.models.generate_content
        mock_client.models.generate_content.side_effect = [mock_response, mock_highlight_response] * 10 
        
        # Run main - we need to mock arXiv fetching too to avoid network calls and flaky data
        with patch('src.main.fetch_latest_papers') as mock_fetch:
            mock_paper = MagicMock()
            mock_paper.title = "Mock Safety Paper"
            mock_paper.summary = "Safety test."
            mock_paper.entry_id = "http://mock"
            mock_paper.published = datetime.datetime.now()
            
            mock_fetch.return_value = [mock_paper]
            
            # Use os.environ patch if necessary, but the code handles missing key gracefully or we can mock it
            with patch.dict(os.environ, {"GOOGLE_API_KEY": "test_key"}):
                # Execute main
                try:
                    main()
                except Exception as e:
                    self.fail(f"Main execution failed: {e}")

if __name__ == '__main__':
    unittest.main()
