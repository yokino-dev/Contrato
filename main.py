from fpdf import FPDF

class ContratoPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'CONTRATO DE LOCAÇÃO DE IMÓVEL RESIDENCIAL', 0, 1, 'C')
        self.ln(5)

def coletar_dados():
    print("--- PREENCHIMENTO DO CONTRATO ---")
    dados = {}
    
    # Qualificação das Partes
    dados['locador_nome'] = input("Nome do Locador: ")
    dados['locador_rg'] = input("RG do Locador: ")
    dados['locador_cpf'] = input("CPF do Locador: ")
    dados['locador_tel'] = input("Telefone do Locador: ")
    
    print("-" * 30)
    dados['inquilino_nome'] = input("Nome do Inquilino: ")
    dados['inquilino_rg'] = input("RG do Inquilino: ")
    dados['inquilino_cpf'] = input("CPF do Inquilino: ")
    dados['inquilino_tel'] = input("Telefone do Inquilino: ")
    
    print("-" * 30)
    # Imóvel
    dados['imovel_rua'] = input("Endereço do Imóvel (Rua, nº, Bairro): ")
    dados['imovel_cidade'] = input("Cidade/UF: ")
    dados['imovel_caract'] = input("Características (ex: 2 quartos, sala...): ")
    
    print("-" * 30)
    # Valores e Prazo
    dados['valor_aluguel'] = input("Valor do Aluguel (ex: 1.200,00): ")
    dados['valor_extenso'] = input("Valor por extenso (ex: mil e duzentos reais): ")
    dados['prazo'] = input("Prazo de validade (ex: 12 meses): ")
    
    return dados

def gerar_contrato(dados):
    pdf = ContratoPDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 10)
    
    # --- SEÇÃO 1: QUALIFICAÇÃO ---
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 7, '1. PARTES CONTRATANTES', 0, 1, 'L')
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "LOCADOR: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, f"{dados['locador_nome']}, portador do RG nº {dados['locador_rg']} e CPF nº {dados['locador_cpf']}, Telefone: {dados['locador_tel']}.\n")
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "INQUILINO: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, f"{dados['inquilino_nome']}, portadora do RG nº {dados['inquilino_rg']} e CPF nº {dados['inquilino_cpf']}, Telefone: {dados['inquilino_tel']}.\n")
    pdf.ln(5)

    # --- SEÇÃO 2: IMÓVEL ---
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 7, '2. DO IMÓVEL', 0, 1, 'L')
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "LOCALIZAÇÃO: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, f"{dados['imovel_rua']}, {dados['imovel_cidade']}.\n")
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "CARACTERÍSTICAS: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, f"{dados['imovel_caract']}.\n")
    pdf.ln(5)

    # --- SEÇÃO 3: VALORES ---
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 7, '3. VALOR E VIGÊNCIA', 0, 1, 'L')
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "VALOR DO ALUGUEL: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, f"R$ {dados['valor_aluguel']} ({dados['valor_extenso']}) mensais.\n")
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "PRAZO DE PERMANÊNCIA: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, f"O contrato terá validade de {dados['prazo']}, renováveis por igual período.\n")
    pdf.ln(5)

    # --- SEÇÃO 4: REGRAS ---
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 7, '4. REGRAS DE MORADIA E CONDIÇÕES DETALHADAS', 0, 1, 'L')
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "4.1. Despesas e Encargos (Contas): ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "O LOCATÁRIO assume a responsabilidade integral pelo pagamento das faturas de água, energia elétrica e demais taxas de consumo a partir da data de entrega das chaves.\n")
    pdf.ln(2)

    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "4.2. Conservação e Manutenção do Imóvel:\n")
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "- Estado de Entrega: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "O inquilino declara receber o imóvel em perfeitas condições de uso, conforme laudo de vistoria (se houver).\n")
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "- Reparos de Uso: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "Danos decorrentes de mau uso, negligência ou causados por terceiros/visitantes são de responsabilidade exclusiva do inquilino.\n")
    pdf.ln(2)

    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "4.3. Devolução do Imóvel: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "Ao término do contrato, o imóvel deve ser entregue totalmente livre de objetos pessoais, limpo e com a pintura nas mesmas cores e condições do início da locação.\n")
    
    pdf.ln(20)

    # --- SEÇÃO 5: ASSINATURAS ---
    y_assinatura = pdf.get_y()
    if y_assinatura > 250: pdf.add_page(); y_assinatura = 30
    
    pdf.line(20, y_assinatura, 90, y_assinatura)
    pdf.set_xy(20, y_assinatura + 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(70, 5, 'LOCADOR', 0, 0, 'C')
    
    pdf.line(120, y_assinatura, 190, y_assinatura)
    pdf.set_xy(120, y_assinatura + 2)
    pdf.cell(70, 5, 'INQUILINO', 0, 1, 'C')

    nome_arquivo = f"contrato_{dados['inquilino_nome'].replace(' ', '_')}.pdf"
    pdf.output(nome_arquivo)
    print(f"\nSucesso! Arquivo '{nome_arquivo}' gerado.")

if __name__ == "__main__":
    dados_coletados = coletar_dados()
    gerar_contrato(dados_coletados)