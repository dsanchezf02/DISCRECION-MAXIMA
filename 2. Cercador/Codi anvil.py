from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go
import anvil.server

class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.ratio = 110  

    def text_box_1_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        query = self.query.text
        
        
        self.ratio -= 10
        
        proportion = self.ratio  
        
        
        for i in range(1, 21):
            getattr(self, f"rich_text_{i}").clear()

        
        anvil.server.call('update_query', query)

        
        results = anvil.server.call('blended_search', query, proportion, count=10)
        for i, result in enumerate(results[:10], start=1):
            title = result['title']
            url = result['link']
            self.set_result(i, title, url)

        start_index = self.rich_text_20.content.find("[")
        end_index = self.rich_text_20.content.find("]")
        enlace1 = self.rich_text_20.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_18.content.find("[")
        end_index = self.rich_text_18.content.find("]")
        enlace2 = self.rich_text_18.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_16.content.find("[")
        end_index = self.rich_text_16.content.find("]")
        enlace3 = self.rich_text_16.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_14.content.find("[")
        end_index = self.rich_text_14.content.find("]")
        enlace4 = self.rich_text_14.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_12.content.find("[")
        end_index = self.rich_text_12.content.find("]")
        enlace5 = self.rich_text_12.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_10.content.find("[")
        end_index = self.rich_text_10.content.find("]")
        enlace6 = self.rich_text_10.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_8.content.find("[")
        end_index = self.rich_text_8.content.find("]")
        enlace7 = self.rich_text_8.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_6.content.find("[")
        end_index = self.rich_text_6.content.find("]")
        enlace8 = self.rich_text_6.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_4.content.find("[")
        end_index = self.rich_text_4.content.find("]")
        enlace9 = self.rich_text_4.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_2.content.find("[")
        end_index = self.rich_text_2.content.find("]")
        enlace10 = self.rich_text_2.content[start_index + 1 : end_index]
        
        anvil.server.call('popups', enlace1, enlace2, enlace3, enlace4, enlace5, enlace6, enlace7, enlace8, enlace9, enlace10)

    def set_result(self, index, title, url):
        rich_text_title = getattr(self, f"rich_text_{index*2-1}")
        rich_text_title.content = title
        rich_text_url = getattr(self, f"rich_text_{index*2}")
        rich_text_url.content = f"[{url}]({url} '{{target=_blank}}')"

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.rich_text_1.content = ""
        self.rich_text_2.content = ""
        self.rich_text_3.content = ""
        self.rich_text_4.content = ""
        self.rich_text_5.content = ""
        self.rich_text_6.content = ""
        self.rich_text_7.content = ""
        self.rich_text_8.content = ""
        self.rich_text_9.content = ""
        self.rich_text_10.content = ""
        self.rich_text_11.content = ""
        self.rich_text_12.content = ""
        self.rich_text_13.content = ""
        self.rich_text_14.content = ""
        self.rich_text_15.content = ""
        self.rich_text_16.content = ""
        self.rich_text_17.content = ""
        self.rich_text_18.content = ""
        self.rich_text_19.content = ""
        self.rich_text_20.content = ""
          
        self.query.text = ""
        self.ratio = 110

    def primary_color_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        query = self.query.text
        
        
        self.ratio -= 10
        
        proportion = self.ratio  
        
        
        for i in range(1, 21):
            getattr(self, f"rich_text_{i}").clear()

        
        anvil.server.call('update_query', query)

        anvil.server.call('write')

        start_index = self.rich_text_20.content.find("[")
        end_index = self.rich_text_20.content.find("]")
        enlace1 = self.rich_text_20.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_18.content.find("[")
        end_index = self.rich_text_18.content.find("]")
        enlace2 = self.rich_text_18.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_16.content.find("[")
        end_index = self.rich_text_16.content.find("]")
        enlace3 = self.rich_text_16.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_14.content.find("[")
        end_index = self.rich_text_14.content.find("]")
        enlace4 = self.rich_text_14.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_12.content.find("[")
        end_index = self.rich_text_12.content.find("]")
        enlace5 = self.rich_text_12.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_10.content.find("[")
        end_index = self.rich_text_10.content.find("]")
        enlace6 = self.rich_text_10.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_8.content.find("[")
        end_index = self.rich_text_8.content.find("]")
        enlace7 = self.rich_text_8.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_6.content.find("[")
        end_index = self.rich_text_6.content.find("]")
        enlace8 = self.rich_text_6.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_4.content.find("[")
        end_index = self.rich_text_4.content.find("]")
        enlace9 = self.rich_text_4.content[start_index + 1 : end_index]
        
        start_index = self.rich_text_2.content.find("[")
        end_index = self.rich_text_2.content.find("]")
        enlace10 = self.rich_text_2.content[start_index + 1 : end_index]
        
        anvil.server.call('popups', enlace1, enlace2, enlace3, enlace4, enlace5, enlace6, enlace7, enlace8, enlace9, enlace10)

        
        results = anvil.server.call('blended_search', query, proportion, count=10)
        for i, result in enumerate(results[:10], start=1):
            title = result['title']
            url = result['link']
            self.set_result(i, title, url)
