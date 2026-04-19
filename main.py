from fpdf import FPDF
from datetime import datetime

class ContratoPDF(FPDF):
    def header(self):
        # Título ajustado para 18 (proporcional)
        self.set_font('Arial', 'B', 18)
        self.cell(0, 12, 'CONTRATO DE LOCAÇÃO DE IMÓVEL RESIDENCIAL', 0, 1, 'C')
        self.ln(2)

def coletar_dados():
    print("\n" + "="*40)
    print("      GERADOR DE CONTRATO (AJUSTE FINO)")
    print("="*40)
    d = {}
    
    d['locador_nome'] = input("Nome do Locador: ")
    d['locador_rg']   = input("RG do Locador: ")
    d['locador_cpf']  = input("CPF do Locador: ")
    d['locador_tel']  = input("Telefone do Locador: ")
    
    print("-" * 20)
    d['inquilino_nome'] = input("Nome do Inquilino: ")
    d['inquilino_rg']   = input("RG do Inquilino: ")
    d['inquilino_cpf']  = input("CPF do Inquilino: ")
    d['inquilino_tel']  = input("Telefone do Inquilino: ")
    
    d['imovel_rua']    = input("Endereço (Rua, nº, Bairro): ")
    d['imovel_cidade'] = input("Cidade/UF: ")
    d['imovel_caract'] = input("Características: ")
    
    d['valor_aluguel'] = input("Valor do Aluguel: ")
    d['valor_extenso'] = input("Valor por extenso: ")
    d['prazo_meses']   = input("Quantidade de meses: ")
    d['data_inicio']   = input("Data de Início: ")
    d['data_fim']      = input("Data de Término: ")
    d['cidade_assinatura'] = input("Cidade para o fechamento: ")
    
    return d

def gerar_contrato(dados):
    # Margens levemente maiores para o texto não ficar "colado" na borda
    pdf = ContratoPDF()
    pdf.set_margins(20, 15, 20)
    pdf.add_page()
    
    # --- CONFIGURAÇÃO DE TAMANHOS (Ajuste para 1 folha) ---
    TAMANHO_TITULO = 16
    TAMANHO_TEXTO = 13
    ALTURA_LINHA = 7  # Reduzido de 8 para 7 para garantir o encaixe
    
    # --- SEÇÃO 1: QUALIFICAÇÃO ---
    pdf.set_font('Arial', 'B', TAMANHO_TITULO)
    pdf.cell(0, 10, '1. PARTES CONTRATANTES', 0, 1, 'L')
    pdf.set_font('Arial', 'B', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, "LOCADOR: ")
    pdf.set_font('Arial', '', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, f"{dados['locador_nome']}, portador do RG nº {dados['locador_rg']} e CPF nº {dados['locador_cpf']}, Telefone: {dados['locador_tel']}.\n")
    pdf.set_font('Arial', 'B', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, "INQUILINO: ")
    pdf.set_font('Arial', '', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, f"{dados['inquilino_nome']}, portadora do RG nº {dados['inquilino_rg']} e CPF nº {dados['inquilino_cpf']}, Telefone: {dados['inquilino_tel']}.\n")
    pdf.ln(4)

    # --- SEÇÃO 2: DO IMÓVEL ---
    pdf.set_font('Arial', 'B', TAMANHO_TITULO)
    pdf.cell(0, 10, '2. DO IMÓVEL', 0, 1, 'L')
    pdf.set_font('Arial', 'B', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, "LOCALIZAÇÃO: ")
    pdf.set_font('Arial', '', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, f"{dados['imovel_rua']}, {dados['imovel_cidade']}.\n")
    pdf.set_font('Arial', 'B', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, "CARACTERÍSTICAS: ")
    pdf.set_font('Arial', '', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, f"{dados['imovel_caract']}.\n")
    pdf.ln(4)

    # --- SEÇÃO 3: VALOR E VIGÊNCIA ---
    pdf.set_font('Arial', 'B', TAMANHO_TITULO)
    pdf.cell(0, 10, '3. VALOR E VIGÊNCIA', 0, 1, 'L')
    pdf.set_font('Arial', 'B', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, "VALOR DO ALUGUEL: ")
    pdf.set_font('Arial', '', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, f"R$ {dados['valor_aluguel']} ({dados['valor_extenso']}) mensais, reajustado anualmente pelo IPCA/IBGE.\n")
    pdf.set_font('Arial', 'B', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, "PRAZO DE PERMANÊNCIA: ")
    pdf.set_font('Arial', '', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, f"{dados['prazo_meses']}, iniciando em {dados['data_inicio']} e com término em {dados['data_fim']}.\n")
    pdf.ln(4)

    # --- SEÇÃO 4: REGRAS E OBRIGAÇÕES (TEXTO ORIGINAL) ---
    pdf.set_font('Arial', 'B', TAMANHO_TITULO)
    pdf.cell(0, 10, '4. REGRAS DE MORADIA E CONDIÇÕES DETALHADAS', 0, 1, 'L')
    pdf.set_font('Arial', 'B', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, "4.1. Destinação: ")
    pdf.set_font('Arial', '', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, "Uso exclusivamente RESIDENCIAL, vedada alteração de finalidade. (Art. 23, II)\n")
    pdf.set_font('Arial', 'B', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, "4.2. Contas e Encargos: ")
    pdf.set_font('Arial', '', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, "Responsabilidade integral do inquilino pelas faturas de consumo (água, luz). (Art. 23, VIII)\n")
    pdf.set_font('Arial', 'B', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, "4.3. Conservação e Manutenção:\n")
    pdf.set_font('Arial', 'B', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, "- Estado de Entrega: "); pdf.set_font('Arial', '', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, "Recebido em perfeitas condições de higiene e funcionamento. (Art. 22, I)\n")
    pdf.set_font('Arial', 'B', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, "- Reparos: "); pdf.set_font('Arial', '', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, "Danos por mau uso são do inquilino. Estruturais cabem ao LOCADOR. (Art. 23, V)\n")
    pdf.set_font('Arial', 'B', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, "4.4. Devolução: "); pdf.set_font('Arial', '', TAMANHO_TEXTO); pdf.write(ALTURA_LINHA, "Imóvel limpo, sem objetos e pintura original, salvo desgaste natural. (Art. 23, III)\n")
    
    # Espaçamento para assinaturas
    pdf.ln(12)

    # --- SEÇÃO 5: ASSINATURAS ---
    y_assinatura = pdf.get_y()
    # Proteção para não quebrar a página bem na assinatura
    if y_assinatura > 255: 
        pdf.add_page()
        y_assinatura = 30
    
    pdf.line(20, y_assinatura, 90, y_assinatura)
    pdf.set_xy(20, y_assinatura + 2)
    pdf.set_font('Arial', 'B', TAMANHO_TEXTO)
    pdf.cell(70, 7, 'LOCADOR', 0, 0, 'C')
    
    pdf.line(120, y_assinatura, 190, y_assinatura)
    pdf.set_xy(120, y_assinatura + 2)
    pdf.cell(70, 7, 'INQUILINO', 0, 1, 'C')

    # Data Final
    pdf.ln(10)
    data_hoje = datetime.now().strftime('%d/%m/%Y')
    pdf.set_font('Arial', '', TAMANHO_TEXTO)
    pdf.cell(0, 10, f"{dados['cidade_assinatura']}, {data_hoje}.", 0, 1, 'C')

    nome_final = f"contrato_{dados['inquilino_nome'].replace(' ', '_')}.pdf"
    pdf.output(nome_final)
    print(f"\nSucesso! PDF gerado em 1 página com fonte 13pt: {nome_final}")

if __name__ == "__main__":
    try:
        dados_preenchidos = coletar_dados()
        gerar_contrato(dados_preenchidos)
    except Exception as e:
        print(f"Erro: {e}")
