from fpdf import FPDF
from datetime import datetime

class ContratoPDF(FPDF):
    def header(self):
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
    d['imovel_caract'] = input("Características (ex: Casa com 2 quartos): ")
    
    # 3. Valores e Prazos
    print("\n[3] VALORES E DATAS")
    d['valor_aluguel'] = input("Valor do Aluguel (ex: 1.200,00): ")
    d['valor_extenso'] = input("Valor por extenso: ")
    d['prazo_meses']   = input("Quantidade de meses (ex: 12 meses): ")
    d['data_inicio']   = input("Data de Início (dd/mm/aaaa): ")
    d['data_fim']      = input("Data de Término (dd/mm/aaaa): ")
    d['cidade_assinatura'] = input("Cidade para o fechamento (ex: São Paulo): ")
    
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
    pdf.set_font('Arial', '', 10); pdf.write(5, f"{dados['prazo_meses']}, iniciando em {dados['data_inicio']} e com término em {dados['data_fim']}.\n")
    pdf.ln(5)

    # --- SEÇÃO 4: REGRAS E OBRIGAÇÕES (LEI 8.245/91) ---
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 7, '4. REGRAS DE MORADIA E CONDIÇÕES DETALHADAS', 0, 1, 'L')
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "4.1. Destinação: ")
    pdf.set_font('Arial', '', 10); pdf.write(5, "Uso exclusivamente RESIDENCIAL, vedada alteração de finalidade. (Art. 23, II)\n")
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "4.2. Contas e Encargos: ")
    pdf.set_font('Arial', '', 10); pdf.write(5, "Responsabilidade integral do inquilino pelas faturas de consumo (água, luz). (Art. 23, VIII)\n")
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "4.3. Conservação e Manutenção:\n")
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "- Estado de Entrega: "); pdf.set_font('Arial', '', 10); pdf.write(5, "Recebido em perfeitas condições de higiene e funcionamento. (Art. 22, I)\n")
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "- Reparos: "); pdf.set_font('Arial', '', 10); pdf.write(5, "Danos por mau uso são do inquilino. Estruturais cabem ao LOCADOR. (Art. 23, V)\n")
    pdf.set_font('Arial', 'B', 10); pdf.write(5, "4.4. Devolução: "); pdf.set_font('Arial', '', 10); pdf.write(5, "Imóvel limpo, sem objetos e pintura original, salvo desgaste natural. (Art. 23, III)\n")
    
    pdf.ln(15)

    # --- SEÇÃO 5: ASSINATURAS ---
    y_assinatura = pdf.get_y()
    if y_assinatura > 240: pdf.add_page(); y_assinatura = 30
    
    pdf.line(20, y_assinatura, 90, y_assinatura)
    pdf.set_xy(20, y_assinatura + 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(70, 5, 'LOCADOR', 0, 0, 'C')
    
    pdf.line(120, y_assinatura, 190, y_assinatura)
    pdf.set_xy(120, y_assinatura + 2)
    pdf.cell(70, 5, 'INQUILINO', 0, 1, 'C')

    # Data Final Centralizada
    pdf.ln(15)
    data_hoje = datetime.now().strftime('%d de %B de %Y') # Pega a data atual do sistema
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 10, f"{dados['cidade_assinatura']}, {data_hoje}.", 0, 1, 'C')

    nome_final = f"contrato_{dados['inquilino_nome'].replace(' ', '_')}.pdf"
    pdf.output(nome_final)
    print(f"\nSucesso! PDF gerado: {nome_final}")

if __name__ == "__main__":
    try:
        dados_preenchidos = coletar_dados()
        gerar_contrato(dados_preenchidos)
    except Exception as e:
        print(f"Erro: {e}")