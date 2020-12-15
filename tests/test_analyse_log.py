from src.analyse_log import analyse_log
import pytest


def test_validar_conteudo_do_arquivo_gerado():
    analyse_log('data/orders_1.csv')
    FILE_TXT = "data/mkt_campaign.txt"
    with open(FILE_TXT) as f:
        file_txt_file = f.readlines()
    assert "hamburguer\n" in file_txt_file
    assert "0\n" in file_txt_file


def test_validar_arquivo_inexistente():
    expect_text = (
           "No such file or directory: "
           "\'data/orders_3.csv\'"
         )
    with pytest.raises(FileNotFoundError, match=expect_text):
        assert analyse_log("data/orders_3.csv")


def test_validar_arquivo_com_extensao_invalida():
    expect_text = (
               "No such file or directory: "
               "\'data/orders_1.txt\'"
             )
    with pytest.raises(FileNotFoundError, match=expect_text):
        assert analyse_log("data/orders_1.txt")
