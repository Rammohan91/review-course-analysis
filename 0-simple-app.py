import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text = "Analysis of Course Reviews", classes = "text-h3 text-center q-pt-md")
    p1 = jp.QDiv(a=wp, text = "These graph represents course review analysis", classes = "text-h5 text-center q-pt-md")

    return wp

jp.justpy(app)