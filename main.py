def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    m_num = int(input('Input number of male students: '))
    f_num = int(input('Input number of female students: '))

    total = m_num + f_num

    m_perc = m_num/total * 100
    f_perc = f_num/total * 100

    print(f'The total number of students is {total}')
    print(f'The total number of male students is {m_num}, and the total number of female students is {f_num}')
    print(f'The percentage of male students is {m_perc:.2f} and the percentage of female students is {f_perc:.2f}')

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
