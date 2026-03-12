import webview # Primeiro instale: pip install pywebview

# Carrega o seu arquivo HTML
webview.create_window('7ª B | Dashboard Ultra', 'index.html', 
                       width=1000, height=700, 
                       resizable=True)

webview.start()
