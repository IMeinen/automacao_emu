# -*- coding: utf-8 -*-
from behave import given, when, then
from action import MinhaAction

''' O método executa os testes da features e apresenta os resultados '''


@given('que tenho permissão para acessar o Google')
def step_impl(context):
    context.obj = MinhaAction()
    context.obj.pesquisar()


@when('acesso o site da Zallpy')
def step_impl(context):
    context.obj.acessar_site()

#
# @when('seleciono a aba oportunidades verificando as vagas disponiveis')
# def step_impl(context):
#     context.obj.acessar_oportunidades()
#
#
# @then('as vagas de {tipo_vaga} são encontradas com sucesso')
# def step_impl(context, tipo_vaga):
#     assert context.obj.validar_vaga_dev(tipo_vaga) is True


@when('seleciono a aba oportunidades verificando vagas de desenvolvedor')
def step_impl(context):
    context.obj.acessar_oportunidades()


@then('as vagas de desenvolvedor são encontradas com sucesso')
def step_impl(context):
    assert context.obj.validar_vagas() is True
