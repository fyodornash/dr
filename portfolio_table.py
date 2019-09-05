import dash_design_kit as ddk
import dash_table.FormatTemplate as FormatTemplate


DEFAULT_ROW = {
    'asset_id': '',
    'ticker_display': '',
    'asset_class': '',
    'returns': '',
    'scenario.min_weight': '',
    'scenario.max_weight': '',
    'additional_scenarios.0.min_weight': '',
    'additional_scenarios.0.max_weight': '',
    'additional_portfolios.0.portfolio_weights': '',
    'additional_portfolios.1.portfolio_weights': ''
}

asset_classes = ['Cash', 'Equity', 'FI', 'RE', 'Com']

NEW_DATA = [{'asset_class': 'Cash',
  'portfolio.0.portfolio_weights': 10,
  'portfolio.1.portfolio_weights': 10,
  'portfolios.2.portfolio_weights': 10,
  'returns': 0.035153294017979446,
  'scenario.0.max_weight': 80,
  'scenario.0.min_weight': 20,
  'scenario.1.max_weight': 80,
  'scenario.1.min_weight': 40,
  'ticker_display': 'OKED'},
 {'asset_class': 'Equity',
  'portfolio.0.portfolio_weights': 10,
  'portfolio.1.portfolio_weights': 10,
  'portfolios.2.portfolio_weights': 10,
  'returns': 0.032706754042141205,
  'scenario.0.max_weight': 100,
  'scenario.0.min_weight': 40,
  'scenario.1.max_weight': 60,
  'scenario.1.min_weight': 0,
  'ticker_display': 'TXRT'},
 {'asset_class': 'Equity',
  'portfolio.0.portfolio_weights': 10,
  'portfolio.1.portfolio_weights': 10,
  'portfolios.2.portfolio_weights': 10,
  'returns': 0.04670273891878958,
  'scenario.0.max_weight': 90,
  'scenario.0.min_weight': 30,
  'scenario.1.max_weight': 70,
  'scenario.1.min_weight': 30,
  'ticker_display': 'RQCJ'},
 {'asset_class': 'FI',
  'portfolio.0.portfolio_weights': 10,
  'portfolio.1.portfolio_weights': 10,
  'portfolios.2.portfolio_weights': 10,
  'returns': 0.04749456152128871,
  'scenario.0.max_weight': 50,
  'scenario.0.min_weight': 30,
  'scenario.1.max_weight': 70,
  'scenario.1.min_weight': 30,
  'ticker_display': 'AQOF'},
 {'asset_class': 'Equity',
  'portfolio.0.portfolio_weights': 10,
  'portfolio.1.portfolio_weights': 10,
  'portfolios.2.portfolio_weights': 10,
  'returns': 0.05682422110866914,
  'scenario.0.max_weight': 70,
  'scenario.0.min_weight': 0,
  'scenario.1.max_weight': 80,
  'scenario.1.min_weight': 40,
  'ticker_display': 'GJKU'},
 {'asset_class': 'Equity',
  'portfolio.0.portfolio_weights': 10,
  'portfolio.1.portfolio_weights': 10,
  'portfolios.2.portfolio_weights': 10,
  'returns': 0.06600596044234555,
  'scenario.0.max_weight': 60,
  'scenario.0.min_weight': 0,
  'scenario.1.max_weight': 70,
  'scenario.1.min_weight': 0,
  'ticker_display': 'IJZC'},
 {'asset_class': 'RE',
  'portfolio.0.portfolio_weights': 10,
  'portfolio.1.portfolio_weights': 10,
  'portfolios.2.portfolio_weights': 10,
  'returns': 0.04041629757562225,
  'scenario.0.max_weight': 80,
  'scenario.0.min_weight': 30,
  'scenario.1.max_weight': 70,
  'scenario.1.min_weight': 10,
  'ticker_display': 'GWBC'},
 {'asset_class': 'FI',
  'portfolio.0.portfolio_weights': 10,
  'portfolio.1.portfolio_weights': 10,
  'portfolios.2.portfolio_weights': 10,
  'returns': 0.05712998623014589,
  'scenario.0.max_weight': 100,
  'scenario.0.min_weight': 20,
  'scenario.1.max_weight': 90,
  'scenario.1.min_weight': 40,
  'ticker_display': 'UCJN'},
 {'asset_class': 'Equity',
  'portfolio.0.portfolio_weights': 10,
  'portfolio.1.portfolio_weights': 10,
  'portfolios.2.portfolio_weights': 10,
  'returns': 0.058264061158547015,
  'scenario.0.max_weight': 70,
  'scenario.0.min_weight': 30,
  'scenario.1.max_weight': 70,
  'scenario.1.min_weight': 20,
  'ticker_display': 'THSA'},
 {'asset_class': 'FI',
  'portfolio.0.portfolio_weights': 10,
  'portfolio.1.portfolio_weights': 10,
  'portfolios.2.portfolio_weights': 10,
  'returns': 0.05819095066893451,
  'scenario.0.max_weight': 80,
  'scenario.0.min_weight': 40,
  'scenario.1.max_weight': 90,
  'scenario.1.min_weight': 30,
  'ticker_display': 'QNIW'}]


FLAT_SAMPLE_PORTFOLIO = [
    {
        'asset_id': 'MS-F00000NFN4',
        'ticker_display': 'BSCL',
        'asset_class': 'FI',
        'returns': 5.3,
        'scenario.min_weight': 0,
        'scenario.max_weight': 50,
        'additional_scenarios.0.min_weight': 0,
        'additional_scenarios.0.max_weight': 100,
        'additional_portfolios.0.portfolio_weights': 50,
        'additional_portfolios.1.portfolio_weights': 70,
        'additional_portfolios.2.portfolio_weights': 90
    },
        {'asset_id': 'IV-IVZ_LDI_USDB_CITIAA_D10',
        'mstar_id': None,
        'ticker_display': 'US DB 10Y',
        'asset_class': 'FI',
        'classification': 'US FI',
        'asset_name': 'US DB LDI RSCG 10Y Citi AA US AA',
        'asset_group': None,
        'risk_coverage': 'IVZ_LDI_USDB_CITIAA_D10',
        'return_coverage': False,
        'benchmark': 0,
        'portfolio': 30,
        'model_return': 4.5,
        'scenario': {'scenario_display': 'Scenario 1',
        'scenario_id': 'scenario_1',
        'return': 4.8,
        'min_weight': 0,
        'max_weight': 100},
        'classification_options': {'options': [{'label': 'Global FI',
         'value': 'GLOBAL'},
        {'label': 'US FI', 'value': 'US'},
        {'label': 'FI', 'value': 'CPA'}]},
        'risk_coverage_options': [{'label': 'Holdings - BMRK',
        'value': 'IVZ_LDI_USDB_CITIAA_D10'}],
        'scenario.return': 4.8,
        'scenario.min_weight': 0,
        'scenario.max_weight': 100,
        'additional_scenarios.0.return': 4.8,
        'additional_scenarios.0.min_weight': 0,
        'additional_scenarios.0.max_weight': 100,
        'additional_portfolios.0.portfolio_weights': 0,
        'additional_portfolios.1.portfolio_weights': 10,
        'additional_portfolios.2.portfolio_weights': 5}]


def portfolio_table():
    columns = [
        # these column IDs _must_ match the portfolio in the `schema`
        {
            'id': 'ticker_display',
            'name': ['Portfolio', 'Ticker'],
        },

        {
            'id': 'asset_class',
            'presentation': 'dropdown',
            'name': ['Portfolio', 'Asset Class'],
        },

        {
            'id': 'returns',
            'name': ['Portfolio', 'Returns'],
            'type': 'numeric',
            'format': FormatTemplate.percentage(1)
        },


        {
            'id': 'scenario.0.min_weight',
            'name': ['Scenario 1', 'Min Wt'],
        },

        {
            'id': 'scenario.0.max_weight',
            'name': ['Scenario 1', 'Max Wt'],
        },


        {
            'id': 'scenario.1.min_weight',
            'name': ['Scenario 2', 'Min Wt'],
        },

        {
            'id': 'scenario.1.max_weight',
            'name': ['Scenario 2', 'Max Wt'],
        },

        {
            'id': 'portfolio.0.portfolio_weights',
            'name': ['Portfolios', 'Portfolio 1'],
        },

        {
            'id': 'portfolio.1.portfolio_weights',
            'name': ['Portfolios', 'Portfolio 2'],
        }
    ]
    data = [DEFAULT_ROW] * 10

    # return DataTable(
    #                 id='portfolio-table',
    #                 merge_duplicate_headers=True,
    #                 columns=columns,
    #                 data=data,
    #                 editable=True,
    #             )

    return ddk.DataTable(
        columns=columns,
        data=NEW_DATA + data[0:2],
        merge_duplicate_headers=True,
        editable=True,
        id='portfolio-table',
        style_cell_conditional=[
            {'if': {'column_id': c['id']},
             'minWidth': '150px', 'width': '150px', 'maxWidth': '150px',}
        for c in columns],
        style_table={
            'overflowX': 'scroll'
        },
        dropdown={
            'asset_class': {
                'options': [
                    {'label': i, 'value': i}
                    for i in asset_classes
                ]
            }
        }
    )