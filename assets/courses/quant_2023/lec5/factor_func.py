# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


def double_sort(df, sort1, sort2='size', group_date='ym', merge_cols=['secID','ret_date']):
    """
    Double sorting.
    Arguments:
        sort1: variable 1 for sorting into 3 groups
        sort2: default is "size", sorting into 2 groups
        group_date: the dates upon which the factor exposures are sorted
        merge_cols: the columns
    returns:
        portfolios containing 2*3 groups
    """
    q1 = dict()
    keys = [f'q_{sort1}_1',f'q_{sort1}_2']
    values = [0.3, 0.7]
    q1.update(zip(keys,values))

    q2 = dict()
    keys = [f'q_{sort2}_1']
    values = [0.5]
    q2.update(zip(keys,values))

    q1_df = pd.DataFrame()
    for key, value in q1.items():
        q1_df[key] = df.groupby([group_date])[sort1].quantile(value)

    q2_df = pd.DataFrame()
    for key, value in q2.items():
        q2_df[key] = df.groupby([group_date])[sort2].quantile(value)

    ret_df_q = pd.merge(df, q2_df, on=group_date)
    ret_df_q = pd.merge(ret_df_q, q1_df, on=group_date)

    portfolios1 = dict()
    portfolios1[f'{sort1}1'] = ret_df_q.loc[ret_df_q[f'{sort1}'] <= ret_df_q[f'q_{sort1}_1']]
    portfolios1[f'{sort1}2'] = ret_df_q.loc[(ret_df_q[f'{sort1}'] >= ret_df_q[f'q_{sort1}_1']) & \
                                            (ret_df_q[f'{sort1}'] <= ret_df_q[f'q_{sort1}_2'])]
    portfolios1[f'{sort1}3'] = ret_df_q.loc[ret_df_q[f'{sort1}'] >= ret_df_q[f'q_{sort1}_2']]

    portfolios2 = dict()
    portfolios2[f'{sort2}1'] = ret_df_q.loc[ret_df_q[f'{sort2}'] <= ret_df_q[f'q_{sort2}_1'],
                                            merge_cols+[group_date]+['ret','exret','size','mktcap']]
    portfolios2[f'{sort2}2'] = ret_df_q.loc[ret_df_q[f'{sort2}'] >= ret_df_q[f'q_{sort2}_1'],
                                            merge_cols+[group_date]+['ret','exret','size','mktcap']]

    portfolios = dict()
    for group1 in portfolios1.keys():
        for group2 in portfolios2.keys():
            portfolios[f'{group1}_{group2}'] = pd.merge(portfolios2[group2],
                                                        portfolios1[group1][merge_cols+[f'{sort1}']],
                                                        on=merge_cols)
    return portfolios


def factor(df, sort1, sort2='size', long_high=True, long_only=True):
    """
    Calculate monthly factor return based on double sorting (2*3). Cannot create the "size" factor.
    Arguments:
        df: the dataframe needed for sorting. Should be a monthly dataframe with returns (one month ahead)
            and other sorting variables
        sort1: the factor exposure upon which the securities to be sorted
        sort2: the controlling factor exposure for independent double sorting. The default is "size".
        long_high: long securities with higher values of sort1?
        long_only: long-only factor returns, or long-short factor returns?
    """
    portfolios = double_sort(df=df, sort1=sort1, sort2=sort2)
    portfolios_vwret = {}
    for pf in portfolios.keys():
    #     portfolios[pf].dropna(inplace=True) # 不应该dropna。如果在某个月停牌，分组时在前一个月，并不知道会这样。
        temp = portfolios[pf].groupby('ym')['mktcap'].agg({'mktcap_sum':np.sum})
        portfolios[pf] = pd.merge(portfolios[pf], temp, on='ym')
        portfolios[pf]['weight'] = portfolios[pf]['mktcap'] / portfolios[pf]['mktcap_sum']
        portfolios[pf]['weighted_ret'] = portfolios[pf]['ret'] * portfolios[pf]['weight']
        portfolios_vwret[pf] = portfolios[pf].groupby('ret_date')['weighted_ret'].sum()

    portfolios_vwret_df = pd.DataFrame(np.vstack([pf for pf in portfolios_vwret.values()])).T
    portfolios_vwret_df.index = portfolios_vwret[f'{sort1}1_size1'].index
    portfolios_vwret_df.columns = portfolios_vwret.keys()
    if long_only:
        if long_high:
            factor = (portfolios_vwret_df[f'{sort1}3_{sort2}1'] + portfolios_vwret_df[f'{sort1}3_{sort2}2']) / 2
        else:
            factor = (portfolios_vwret_df[f'{sort1}1_{sort2}1'] + portfolios_vwret_df[f'{sort1}1_{sort2}2']) / 2
    else:
        if long_high:
            factor = (portfolios_vwret_df[f'{sort1}3_{sort2}1'] + portfolios_vwret_df[f'{sort1}3_{sort2}2']) / 2 - \
                     (portfolios_vwret_df[f'{sort1}1_{sort2}1'] + portfolios_vwret_df[f'{sort1}1_{sort2}2']) / 2
        else:
            factor = (portfolios_vwret_df[f'{sort1}1_{sort2}1'] + portfolios_vwret_df[f'{sort1}1_{sort2}2']) / 2 - \
                     (portfolios_vwret_df[f'{sort1}3_{sort2}1'] + portfolios_vwret_df[f'{sort1}3_{sort2}2']) / 2
    factor.name = sort1
    return factor

def daily_factor(sort_df, stock_df, sort1, sort2='size', long_high=True, long_only=True):
    """
    Calculate daily factor return based on double sorting (2*3). Cannot create the "size" factor.
    Arguments:
        sort_df: the dataframe needed for sorting. Should be a monthly dataframe with sorting variables
                 and market capitalization.
        sort1: the factor exposure upon which the securities to be sorted
        sort2: the controlling factor exposure for independent double sorting. The default is "size".
        long_high: long securities with higher values of sort1?
        long_only: long-only factor returns, or long-short factor returns?
    """
    portfolios = double_sort(df=sort_df, sort1=sort1, sort2=sort2)
    portfolios_vwret = {}
    for pf in portfolios.keys():
        temp = portfolios[pf].groupby('ym')['mktcap'].agg({'mktcap_sum':np.sum})
        portfolios[pf] = pd.merge(portfolios[pf], temp, on='ym')
        portfolios[pf]['weight'] = portfolios[pf]['mktcap'] / portfolios[pf]['mktcap_sum']
        df_ = pd.merge(portfolios[pf][['secID','ret_date','weight']],
                       stock_df[['secID','tradeDate','ym','ret_daily']],
                       left_on=['secID','ret_date'],
                       right_on=['secID','ym'])
        df_['weighted_ret_daily'] = df_['ret_daily'] * df_['weight']
        portfolios_vwret[pf] = df_.groupby('tradeDate')['weighted_ret_daily'].sum()

    portfolios_vwret_df = pd.DataFrame(np.vstack([pf for pf in portfolios_vwret.values()])).T
    portfolios_vwret_df.index = portfolios_vwret[list(portfolios_vwret.keys())[0]].index
    portfolios_vwret_df.columns = portfolios_vwret.keys()
    if long_only:
        if long_high:
            factor = (portfolios_vwret_df[f'{sort1}3_{sort2}1'] + portfolios_vwret_df[f'{sort1}3_{sort2}2']) / 2
        else:
            factor = (portfolios_vwret_df[f'{sort1}1_{sort2}1'] + portfolios_vwret_df[f'{sort1}1_{sort2}2']) / 2
    else:
        if long_high:
            factor = (portfolios_vwret_df[f'{sort1}3_{sort2}1'] + portfolios_vwret_df[f'{sort1}3_{sort2}2']) / 2 - \
                     (portfolios_vwret_df[f'{sort1}1_{sort2}1'] + portfolios_vwret_df[f'{sort1}1_{sort2}2']) / 2
        else:
            factor = (portfolios_vwret_df[f'{sort1}1_{sort2}1'] + portfolios_vwret_df[f'{sort1}1_{sort2}2']) / 2 - \
                     (portfolios_vwret_df[f'{sort1}3_{sort2}1'] + portfolios_vwret_df[f'{sort1}3_{sort2}2']) / 2
    factor.name = sort1
    return factor