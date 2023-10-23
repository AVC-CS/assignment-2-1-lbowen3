def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    m_perc = int(input('Input number of male students: '))
    f_perc = int(input('Input number of female students: '))

    total = m_perc + f_perc

    print(f'The total number of students is {total}')
    print(f'The total number of female students is {f_perc}, and the total number of male students is {m_perc}')
    print(f'The percentage of male students is {m_perc/total:.2%} and the percentage of female students is {f_perc/total:.2%}')
    
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
