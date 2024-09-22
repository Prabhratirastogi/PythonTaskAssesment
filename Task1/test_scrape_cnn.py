import unittest
from unittest.mock import patch, Mock
from io import StringIO
from task_1_scrape_news import scrape_cnn_articles

class TestScrapeCNNArticles(unittest.TestCase):

        @patch('task_1_scrape_news.requests.get')
        def test_scrape_cnn_articles_no_articles(self, mock_get):
            # Mock the response with no articles containing the required class
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.text = '''
                <html>
                    <body>
                        <!-- There are no links with class "container__link" -->
                        <a class="other_class" href="#"></a>
                    </body>
                </html>
            '''
            mock_get.return_value = mock_response

            # Capture the output
            with patch('sys.stdout', new=StringIO()) as fake_out:
                scrape_cnn_articles(limit=2)
                output = fake_out.getvalue()

            # Check for no articles found message
            self.assertIn("No articles found with the specified class.", output)
