from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class Calculadora(App):
	def build(self):
		# Criar o layout
		self.layout = BoxLayout(orientation="vertical")
		
		# Área para os botões
		self.buttons = GridLayout(cols=4)
		
		# Textos dos botões
		buttons_texts = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "C", "=", "/", "*", "+", "-"]
		
		# Botão do número 1
		self.um = Button(text=buttons_texts[0])
		
		self.um.bind(on_press=self.click_1)
		
		self.buttons.add_widget(self.um)
		
		# Botão do número 2
		self.dois = Button(text=buttons_texts[1])
		
		self.dois.bind(on_press=self.click_2)
		
		self.buttons.add_widget(self.dois)
		
		# Botão do número 3
		self.tres = Button(text=buttons_texts[2])
		
		self.tres.bind(on_press=self.click_3)
		
		self.buttons.add_widget(self.tres)
		
		# Botão da subtração
		self.sub = Button(text=buttons_texts[15])
		
		self.sub.bind(on_press=self.click_sub)
		
		self.buttons.add_widget(self.sub)
		
		# Botão do número 4
		self.quatro = Button(text=buttons_texts[3])
		
		self.quatro.bind(on_press=self.click_4)
		
		self.buttons.add_widget(self.quatro)
		
		# Botão do número 5
		self.cinco = Button(text=buttons_texts[4])
		
		self.cinco.bind(on_press=self.click_5)
		
		self.buttons.add_widget(self.cinco)
		
		# Botão do número 6
		self.seis = Button(text=buttons_texts[5])
		
		self.seis.bind(on_press=self.click_6)
		
		self.buttons.add_widget(self.seis)
		
		# Botão da multiplicação
		self.mult = Button(text=buttons_texts[13])
		
		self.mult.bind(on_press=self.click_mult)
		
		self.buttons.add_widget(self.mult)
		
		# Botão do número 7
		self.sete = Button(text=buttons_texts[6])
		
		self.sete.bind(on_press=self.click_7)
		
		self.buttons.add_widget(self.sete)
		
		# Botão do 8
		self.oito = Button(text=buttons_texts[7])
		
		self.oito.bind(on_press=self.click_8)
		
		self.buttons.add_widget(self.oito)
		
		# Botão do 9
		self.nove = Button(text=buttons_texts[8])
		
		self.nove.bind(on_press=self.click_9)
		
		self.buttons.add_widget(self.nove)
		
		# Botão da divisão
		self.div = Button(text=buttons_texts[12])
		
		self.div.bind(on_press=self.click_div)
		
		self.buttons.add_widget(self.div)
		
		# Botão do 0
		self.zero = Button(text=buttons_texts[9])
		
		self.zero.bind(on_press=self.click_0)
		
		self.buttons.add_widget(self.zero)
		
		# Botão para limpar tudo
		self.clear = Button(text=buttons_texts[10])
		
		self.clear.bind(on_press=self.click_c)
		
		self.buttons.add_widget(self.clear)
		
		# Botão do =
		self.igual = Button(text=buttons_texts[11])
		
		self.igual.bind(on_press=self.click_igual)
		
		self.buttons.add_widget(self.igual)
		
		# Botão da adição
		self.adic = Button(text=buttons_texts[14])
		
		self.adic.bind(on_press=self.click_adic)
		
		self.buttons.add_widget(self.adic)
		
		# Mostrar as contas
		self.conta = TextInput(size_hint_y=0.3, hint_text="Conta...", readonly=True)
		
		# Adicionar a area para mostrar as contas
		self.layout.add_widget(self.conta)
		
		# Adicionar ao layout principal
		self.layout.add_widget(self.buttons)
		
		return self.layout
	
	def click_1(self, instance):
		self.conta.text += "1"
	
	def click_2(self, instance):
		self.conta.text += "2"
	
	def click_3(self, instance):
		self.conta.text += "3"
	
	def click_4(self, instance):
		self.conta.text += "4"
	
	def click_5(self, instance):
		self.conta.text += "5"
	
	def click_6(self, instance):
		self.conta.text += "6"
	
	def click_7(self, instance):
		self.conta.text += "7"
	
	def click_8(self, instance):
		self.conta.text += "8"
	
	def click_9(self, instance):
		self.conta.text += "9"
	
	def click_0(self, instance):
		self.conta.text += "0"
	
	def click_c(self, instance):
		self.conta.text = ""
	
	def click_sub(self, instance):
		self.conta.text += " - "
	
	def click_mult(self, instance):
		self.conta.text += " * "
	
	def click_adic(self, instance):
		self.conta.text += " + "
	
	def click_div(self, instance):
		self.conta.text += " / "
	
	def click_igual(self, instance):
		try:
			resultado = eval(self.conta.text)
			self.conta.text = f"{resultado}"
		except Exception as e:
			print("erro")

if __name__ == "__main__":
	Calculadora().run()