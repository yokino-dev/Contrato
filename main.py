from fpdf import FPDF
from datetime import datetime
import locale

# Tenta configurar para português para a data sair correta (opcional)
try:
    locale.setlocale(locale.LC_TIME, "pt_BR.utf-8")
except:
    pass

class ContratoPDF(FPDF):
    def header(self):
        # Aumentado de 14 para 16
        self.set_font('Arial', 'B', 16)
        self.cell(0, 12, 'CONTRATO DE LOCAÇÃO DE IMÓVEL RESIDENCIAL', 0, 1, 'C')
        self.ln(3) # Reduzido espaço para caber na folha

def coletar_dados():
    print("\n" + "="*40)
    print("      GERADOR DE CONTRATO DE LOCAÇÃO")
    print("="*40)
    d = {}
    
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
    
    print("\n[2] INFORMAÇÕES DO IMÓVEL")
    d['imovel_rua']    = input("Endereço (Rua, nº, Bairro): ")
    d['imovel_cidade'] = input("Cidade/UF: ")
    d['imovel_caract'] = input("Características: ")
    
    print("\n[3] VALORES E DATAS")
    d['valor_aluguel'] = input("Valor do Aluguel: ")
    d['valor_extenso'] = input("Valor por extenso: ")
    d['prazo_meses']   = input("Quantidade de meses: ")
    d['data_inicio']   = input("Data de Início: ")
    d['data_fim']      = input("Data de Término: ")
    d['cidade_assinatura'] = input("Cidade para o fechamento: ")
    
    return d

def gerar_contrato(dados):
    pdf = ContratoPDF()
    pdf.add_page()
    # Fonte base aumentada de 10 para 12
    pdf.set_font('Arial', '', 12)
    
    # --- SEÇÃO 1: QUALIFICAÇÃO ---
    pdf.set_font('Arial', 'B', 13) # Título de seção aumentado
    pdf.cell(0, 8, '1. PARTES CONTRATANTES', 0, 1, 'L')
    pdf.set_font('Arial', 'B', 12); pdf.write(6, "LOCADOR: ")
    pdf.set_font('Arial', '', 12); pdf.write(6, f"{dados['locador_nome']}, RG nº {dados['locador_rg']}, CPF nº {dados['locador_cpf']}, Tel: {dados['locador_tel']}.\n")
    pdf.set_font('Arial', 'B', 12); pdf.write(6, "INQUILINO: ")
    pdf.set_font('Arial', '', 12); pdf.write(6, f"{dados['inquilino_nome']}, RG nº {dados['inquilino_rg']}, CPF nº {dados['inquilino_cpf']}, Tel: {dados['inquilino_tel']}.\n")
    pdf.ln(4)

    # --- SEÇÃO 2: DO IMÓVEL ---
    pdf.set_font('Arial', 'B', 13)
    pdf.cell(0, 8, '2. DO IMÓVEL', 0, 1, 'L')
    pdf.set_font('Arial', 'B', 12); pdf.write(6, "LOCALIZAÇÃO: ")
    pdf.set_font('Arial', '', 12); pdf.write(6, f"{dados['imovel_rua']}, {dados['imovel_cidade']}.\n")
    pdf.set_font('Arial', 'B', 12); pdf.write(6, "CARACTERÍSTICAS: ")
    pdf.set_font('Arial', '', 12); pdf.write(6, f"{dados['imovel_caract']}.\n")
    pdf.ln(4)

    # --- SEÇÃO 3: VALOR E VIGÊNCIA ---
    pdf.set_font('Arial', 'B', 13)
    pdf.cell(0, 8, '3. VALOR E VIGÊNCIA', 0, 1, 'L')
    pdf.set_font('Arial', 'B', 12); pdf.write(6, "VALOR: ")
    pdf.set_font('Arial', '', 12); pdf.write(6, f"R$ {dados['valor_aluguel']} ({dados['valor_extenso']}) mensais.\n")
    pdf.set_font('Arial', 'B', 12); pdf.write(6, "PRAZO: ")
    pdf.set_font('Arial', '', 12); pdf.write(6, f"{dados['prazo_meses']}, de {dados['data_inicio']} a {dados['data_fim']}.\n")
    pdf.ln(4)

    # --- SEÇÃO 4: REGRAS (Compactado para caber) ---
    pdf.set_font('Arial', 'B', 13)
    pdf.cell(0, 8, '4. REGRAS E CONDIÇÕES', 0, 1, 'L')
    pdf.set_font('Arial', 'B', 12); pdf.write(6, "4.1. Uso: ")
    pdf.set_font('Arial', '', 12); pdf.write(6, "Residencial apenas (Art. 23, II).\n")
    pdf.set_font('Arial', 'B', 12); pdf.write(6, "4.2. Contas: ")
    pdf.set_font('Arial', '', 12); pdf.write(6, "Água e luz por conta do inquilino (Art. 23, VIII).\n")
    pdf.set_font('Arial', 'B', 12); pdf.write(6, "4.3. Manutenção: ")
    pdf.set_font('Arial', '', 12); pdf.write(6, "Danos por mau uso são do inquilino. Estrutura do locador.\n")
    
    # Espaço para assinaturas
    pdf.ln(15)

    # --- SEÇÃO 5: ASSINATURAS ---
    y_assinatura = pdf.get_y()
    # Verifica se vai ultrapassar a folha, se sim, sobe a assinatura
    if y_assinatura > 250: pdf.add_page(); y_assinatura = 40
    
    pdf.line(20, y_assinatura, 90, y_assinatura)
    pdf.set_xy(20, y_assinatura + 2)
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(70, 5, 'LOCADOR', 0, 0, 'C')
    
    pdf.line(120, y_assinatura, 190, y_assinatura)
    pdf.set_xy(120, y_assinatura + 2)
    pdf.cell(70, 5, 'INQUILINO', 0, 1, 'C')

    # Data Final
    pdf.ln(12)
    data_hoje = datetime.now().strftime('%d/%m/%Y')
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f"{dados['cidade_assinatura']}, {data_hoje}.", 0, 1, 'C')

    nome_final = f"contrato_{dados['inquilino_nome'].replace(' ', '_')}.pdf"
    pdf.output(nome_final)
    print(f"\nSucesso! PDF gerado com letras maiores: {nome_final}")

if __name__ == "__main__":
    try:
        dados_preenchidos = coletar_dados()
        gerar_contrato(dados_preenchidos)
    except Exception as e:
        print(f"Erro: {e}")