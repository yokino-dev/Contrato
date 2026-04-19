from fpdf import FPDF

class ContratoPDF(FPDF):
    def header(self):
        # Título em Negrito
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'CONTRATO DE LOCAÇÃO DE IMÓVEL RESIDENCIAL', 0, 1, 'C')
        self.ln(5)

def gerar_contrato():
    pdf = ContratoPDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 10)
    
    # --- SEÇÃO 1: QUALIFICAÇÃO DAS PARTES ---
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 7, '1. PARTES CONTRATANTES', 0, 1, 'L')
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "LOCADOR: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "João da Silva, portador do RG nº 00.000.000-0 e CPF nº 000.000.000-00, Telefone: (11) 99999-9999.\n")
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "INQUILINO: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "Maria Oliveira, portadora do RG nº 11.111.111-1 e CPF nº 111.111.111-11, Telefone: (11) 88888-8888.\n")
    pdf.ln(5)

    # --- SEÇÃO 2: OBJETO E CARACTERÍSTICAS ---
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 7, '2. DO IMÓVEL', 0, 1, 'L')
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "LOCALIZAÇÃO: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "Rua das Flores, nº 123, Bairro Jardim, Cidade/UF.\n")
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "CARACTERÍSTICAS: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "Casa composta por 2 dormitórios, sala de estar, cozinha americana, área de serviço e 1 banheiro social.\n")
    pdf.ln(5)

    # --- SEÇÃO 3: VALORES E PRAZO ---
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 7, '3. VALOR E VIGÊNCIA', 0, 1, 'L')
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "VALOR DO ALUGUEL: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "R$ 1.200,00 (mil e duzentos reais) mensais.\n")
    
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "PRAZO DE PERMANÊNCIA: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "O contrato terá validade de 12 meses, renováveis por igual período.\n")
    pdf.ln(5)

    # --- SEÇÃO 4: REGRAS E OBRIGAÇÕES DETALHADAS ---
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 7, '4. REGRAS DE MORADIA E CONDIÇÕES DETALHADAS', 0, 1, 'L')
    
    # 4.1 Despesas
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "4.1. Despesas e Encargos (Contas): ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "O LOCATÁRIO assume a responsabilidade integral pelo pagamento das faturas de água, energia elétrica e demais taxas de consumo a partir da data de entrega das chaves.\n")
    pdf.ln(2)

    # 4.2 Manutenção
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

    # 4.3 Devolução
    pdf.set_font('Arial', 'B', 10)
    pdf.write(5, "4.3. Devolução do Imóvel: ")
    pdf.set_font('Arial', '', 10)
    pdf.write(5, "Ao término do contrato, o imóvel deve ser entregue totalmente livre de objetos pessoais, limpo e com a pintura nas mesmas cores e condições do início da locação.\n")
    
    pdf.ln(15)

    # --- SEÇÃO 5: ASSINATURAS ---
    y_assinatura = pdf.get_y()
    
    # Garantir que as assinaturas não fiquem coladas no fim da página
    if y_assinatura > 250:
        pdf.add_page()
        y_assinatura = 30

    # Linha do Locador
    pdf.line(20, y_assinatura, 90, y_assinatura)
    pdf.set_xy(20, y_assinatura + 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(70, 5, 'LOCADOR', 0, 0, 'C')
    
    # Linha do Inquilino
    pdf.line(120, y_assinatura, 190, y_assinatura)
    pdf.set_xy(120, y_assinatura + 2)
    pdf.cell(70, 5, 'INQUILINO', 0, 1, 'C')

    # Salvar
    pdf.output('contrato_atualizado.pdf')
    print("PDF 'contrato_atualizado.pdf' gerado com sucesso!")

if __name__ == "__main__":
    gerar_contrato()