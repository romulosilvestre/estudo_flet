#FIXME: cor branca em hexadecimal
#584BD5
import flet as ft
def main(page:ft.Page):
    #RED GREEN BLUE
    #YELLOW
    page.bgcolor = "white"
    page.window_width=400
    page.window_height=400
    linha1 = ft.Row(
        controls=[
            ft.Text("Sabadão da Programação 1")
        ]
    )
    linha2 = ft.Row(
        controls=[
            ft.Text("Sabadão da Programação 2")
        ]
    )
    linha3 = ft.Row(
        controls=[
            ft.Text("Sabadão da Programação 3")
        ]
    )
    linha4 = ft.Row(
        controls=[
            ft.ElevatedButton(text='1',bgcolor=ft.colors.RED,color=ft.colors.WHITE),
            ft.ElevatedButton(text='2',bgcolor=ft.colors.RED,color=ft.colors.WHITE),
            ft.ElevatedButton(text='3',bgcolor=ft.colors.RED,color=ft.colors.WHITE),
            ft.ElevatedButton(text='4',bgcolor=ft.colors.BLACK12,color=ft.colors.WHITE),
            ft.ElevatedButton(text='5',bgcolor=ft.colors.BLACK12,color=ft.colors.WHITE),
            ft.ElevatedButton(text='6',bgcolor=ft.colors.BLACK12,color=ft.colors.WHITE),
            ft.ElevatedButton(text='7',bgcolor=ft.colors.AMBER,color=ft.colors.WHITE),
            ft.ElevatedButton(text='8',bgcolor=ft.colors.AMBER,color=ft.colors.WHITE),
            ft.ElevatedButton(text='9',bgcolor=ft.colors.AMBER,color=ft.colors.WHITE),
            ft.ElevatedButton(text='10',bgcolor=ft.colors.AMBER_200,color=ft.colors.WHITE),
            ft.ElevatedButton(text='11',bgcolor=ft.colors.AMBER_200,color=ft.colors.WHITE),
            ft.ElevatedButton(text='12',bgcolor=ft.colors.AMBER_400,color=ft.colors.WHITE)

        ],
        alignment= ft.MainAxisAlignment.START,
        spacing=20,
        wrap=True,
        run_spacing=4,
        vertical_alignment= ft.CrossAxisAlignment.CENTER,
        #expand=True,
    )
    linha5=ft.Row(
         controls=[
             
             ft.Image(height=200,src='imagens/flet.png'),
             ft.Image(height=200,src='imagens/flask.png'),
             ft.Image(height=200,src='imagens/flet.png'),
             ft.Image(height=200,src='imagens/logopython.jpeg'),
             ft.Image(height=200,src='imagens/flask.png'),
         ],
         scroll=ft.ScrollMode.AUTO,
         auto_scroll=True,
             
       
    )  
    linha5=ft.Row(
         controls=[
             
             ft.Image(height=200,src='imagens/flet.png'),
             ft.Image(height=200,src='imagens/flask.png'),
             ft.Image(height=200,src='imagens/flet.png'),
             ft.Image(height=200,src='imagens/logopython.jpeg'),
             ft.Image(height=200,src='imagens/flask.png')
         ],
         scroll=ft.ScrollMode.AUTO,
         auto_scroll=True,
             
       
    )  
    btn1= ft.ElevatedButton(text='1',bgcolor=ft.colors.RED,color=ft.colors.WHITE)
    btn2 =ft.ElevatedButton(text='2',bgcolor=ft.colors.RED,color=ft.colors.WHITE)
    btn3 =ft.ElevatedButton(text='3',bgcolor=ft.colors.RED,color=ft.colors.WHITE)
 
    mensagem = ft.Text()
    def btn_click(e):
        mensagem.value = "Sabadão no Flet aplicando Cor"
        btn.bgcolor = "YELLOW"
        btn.color = "BLACK"
        page.update()
    btn = ft.ElevatedButton("clique aqui!",color="WHITE",bgcolor="RED",on_click=btn_click)
    page.add(linha1,linha2,linha3,linha4,linha5,btn1,btn2,btn3,btn)
    page.update()

ft.app(target=main)