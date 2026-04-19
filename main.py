from fpdf import FPDF

class ContratoPDF(FPDF):
    def header(self):
        # Título principal do documento
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'CONTRATO DE LOCAÇÃO DE IMÓVEL RESIDENCIAL', 0, 1, 'C')
        self.ln(5)

def coletar_dados():
    print("\n" + "="*40)
    print("      GERADOR DE CONTRATO DE LOCAÇÃO")
    print("="*40)
    d = {}
    
    # 1. Qualificação das Partes
    print("\n[1] INFORMAÇÕES DAS PARTES")
    d['locador_nome'] = input("Nome do Locador: ")
    d['locador_rg']   = input("RG do Locador: ")
    d['locador_cpf']  = input("CPF do Locador: ")
    d['locador_tel']  = input("Telefone do Locador: ")
    
    print("-" * 20)
    d['inquilino_nome'] = input("Nome do Inquilino: ")
    d['inquilino_rg']   = input("RG do Inquilino: ")
    d['inquilino_cpf']  = input("CPF do Inquilino: ")
    d['inquilino_tel']  = input("Telefone do Inquilino: ")
    
    # 2. Dados do Imóvel
    print("\n[2] INFORMAÇÕES DO IMÓVEL")
    d['imovel_rua']    = input("Endereço (Rua, nº, Bairro): ")
    d['imovel_cidade'] = input("Cidade/UF: ")
    d['imovel_caract'] = input("Características (ex: Casa com 2 quartos, sala...): ")
    
    # 3. Valores e Prazos
    print("\n[3] VALORES E PRAZOS")
    d['valor_aluguel'] = input("Valor do Aluguel (ex: 1.200,00): ")
    d['valor_extenso'] = input("Valor por extenso (ex: mil e duzentos reais): ")
    d['prazo']         = input("Prazo de validade (ex: 12 meses): ")
    
    return d

def gerar_contrato(dados):
    pdf = ContratoPDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 10)
    
    # --- SEÇÃO 1: QUALIFICAÇÃO ---
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 7, '1. PARTES CONTRATANTES', 0, 1, 'L')
    
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "LOCADOR: ")
    pdf.set_font('Arial', '', 10); pdf.write(5, f"{dados['locador_nome']}, portador do RG nº {dados['locador_rg']} e CPF nº {dados['locador_cpf']}, Telefone: {dados['locador_tel']}.\n")
    
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "INQUILINO: ")
    pdf.set_font('Arial', '', 10); pdf.write(5, f"{dados['inquilino_nome']}, portadora do RG nº {dados['inquilino_rg']} e CPF nº {dados['inquilino_cpf']}, Telefone: {dados['inquilino_tel']}.\n")
    pdf.ln(5)

    # --- SEÇÃO 2: DO IMÓVEL ---
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 7, '2. DO IMÓVEL', 0, 1, 'L')
    
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "LOCALIZAÇÃO: ")
    pdf.set_font('Arial', '', 10); pdf.write(5, f"{dados['imovel_rua']}, {dados['imovel_cidade']}.\n")
    
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "CARACTERÍSTICAS: ")
    pdf.set_font('Arial', '', 10); pdf.write(5, f"{dados['imovel_caract']}.\n")
    pdf.ln(5)

    # --- SEÇÃO 3: VALOR E VIGÊNCIA ---
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 7, '3. VALOR E VIGÊNCIA', 0, 1, 'L')
    
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "VALOR DO ALUGUEL: ")
    pdf.set_font('Arial', '', 10); pdf.write(5, f"R$ {dados['valor_aluguel']} ({dados['valor_extenso']}) mensais, reajustado anualmente pelo IPCA/IBGE.\n")
    
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "PRAZO DE PERMANÊNCIA: ")
    pdf.set_font('Arial', '', 10); pdf.write(5, f"O contrato terá validade de {dados['prazo']}, podendo ser renovado por igual período mediante acordo entre as partes.\n")
    pdf.ln(5)

    # --- SEÇÃO 4: REGRAS E OBRIGAÇÕES (LEI 8.245/91) ---
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 7, '4. REGRAS DE MORADIA E CONDIÇÕES DETALHADAS', 0, 1, 'L')
    
    # 4.1 Destinação
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "4.1. Destinação: ")
    pdf.set_font('Arial', '', 10); pdf.write(5, "O imóvel destina-se exclusivamente para uso RESIDENCIAL, sendo vedada alteração de finalidade sem autorização. (Art. 23, II)\n")
    pdf.ln(2)

    # 4.2 Contas
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "4.2. Contas e Encargos: ")
    pdf.set_font('Arial', '', 10); pdf.write(5, "O LOCATÁRIO assume a responsabilidade integral pelo pagamento das faturas de água, energia e taxas de consumo. (Art. 23, VIII)\n")
    pdf.ln(2)

    # 4.3 Manutenção
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "4.3. Conservação e Manutenção:\n")
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "- Estado de Entrega: ")
    pdf.set_font('Arial', '', 10); pdf.write(5, "Recebido em perfeitas condições de uso, higiene e funcionamento. (Art. 22, I)\n")
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "- Reparos: ")
    pdf.set_font('Arial', '', 10); pdf.write(5, "Danos por mau uso são de responsabilidade do inquilino. Manutenções estruturais cabem ao LOCADOR. (Art. 23, V)\n")
    pdf.ln(2)

    # 4.4 Devolução
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "4.4. Devolução do Imóvel: ")
    pdf.set_font('Arial', '', 10); pdf.write(5, "Deve ser entregue limpo, sem objetos e com a pintura nas mesmas condições do início, salvo desgaste natural. (Art. 23, III)\n")
    
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

    nome_final = f"contrato_{dados['inquilino_nome'].replace(' ', '_')}.pdf"
    pdf.output(nome_final)
    print(f"\n" + "="*40)
    print(f"Sucesso! PDF gerado: {nome_final}")
    print("="*40)

if __name__ == "__main__":
    try:
        dados_preenchidos = coletar_dados()
        gerar_contrato(dados_preenchidos)
    except Exception as e:
        print(f"Erro ao gerar o contrato: {e}")