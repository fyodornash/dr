import pandas as pd
import numpy as np
import plotly.graph_objects as go
import scipy.optimize as sco

data = pd.read_csv('four-stock-daily.csv')

df = data.set_index('date')

table = df.pivot(columns='ticker')
# By specifying col[1] in below list comprehension
# You can select the stock names under multi-level column
table.columns = [col[1] for col in table.columns]

def portfolio_annualised_performance(weights, mean_returns, cov_matrix):
    returns = np.sum(mean_returns*weights ) *252
    std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
    return std, returns

def portfolio_volatility(weights, mean_returns, cov_matrix):
    return portfolio_annualised_performance(weights, mean_returns, cov_matrix)[0]

def min_variance(mean_returns, cov_matrix, bounds):
    num_assets = len(mean_returns)
    args = (mean_returns, cov_matrix)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

    result = sco.minimize(portfolio_volatility, num_assets*[1./num_assets,], args=args,
                        method='SLSQP', bounds=bounds, constraints=constraints)

    return result

def efficient_return(mean_returns, cov_matrix, target, bounds):
    num_assets = len(mean_returns)
    args = (mean_returns, cov_matrix)

    def portfolio_return(weights):
        return portfolio_annualised_performance(weights, mean_returns, cov_matrix)[1]

    constraints = ({'type': 'eq', 'fun': lambda x: portfolio_return(x) - target},
                   {'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0,1) for asset in range(num_assets))
    result = sco.minimize(portfolio_volatility, num_assets*[1./num_assets,], args=args, method='SLSQP', bounds=bounds, constraints=constraints)
    return result


def efficient_frontier(mean_returns, cov_matrix, returns_range):
    efficients = []
    for ret in returns_range:
        efficients.append(efficient_return(mean_returns, cov_matrix, ret))
    return efficients

# returns = table.pct_change()
# mean_returns = returns.mean()
# cov_matrix = returns.cov()
# risk_free_rate = 0.0178

def plot_efficient_frontiers(data)
    min_vol = min_variance(mean_returns, cov_matrix)
    sdp_min, rp_min = portfolio_annualised_performance(min_vol['x'], mean_returns, cov_matrix)
    target = np.linspace(rp_min, 0.34, 100)
    efficient_portfolios = efficient_frontier(mean_returns, cov_matrix, target)

    weights = [e['x']for e in efficient_portfolios]

    nested_labels = [['{}: {:.2f}'.format(t,w) for t,w in zip(table.columns, weights_i)]  for weights_i in weights]

    labels = ['<b>Weights:</b><br>' + '<br>'.join(l) for l in nested_labels]

    fig = go.Figure(go.Scatter(y=target, x=[p['fun'] for p in efficient_portfolios], text=labels, hoverinfo='text', name='Efficient Frontier'))
    fig = fig.update_layout(xaxis_title_text='Anualized Volitility', yaxis_title_text='Anualized Returns')
    fig = fig.add_scatter(y=mean_returns * 252, x=returns.std() * np.sqrt(252), text=mean_returns.index, mode='markers+text', textposition='top center', showlegend=False)

    return fig