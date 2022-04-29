def label_function(val):
    return f'{val:.0f}%'

fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8), (ax9, ax10), (ax11, ax12), (ax13, ax14)) = plt.subplots(ncols = 2, nrows = 7, figsize = (25, 25))

explode1 = (0, 0.1)
explode2 = (0.15, 0.2)
explode3 = (0, 0.1)
explode4 = (0.1, 0.2)
explode5 = (0.1, 0.1)

df.groupby('Passport').size().plot(kind='pie', autopct=label_function, textprops={'fontsize': 15},
                                  colors=['mediumorchid', 'hotpink'], labels = ["No", "Yes"], shadow=True, explode=explode1, ax=ax1)

df.groupby('Household').size().plot(kind='pie', autopct=label_function, textprops={'fontsize': 15},
                                 colors=['mediumorchid', 'hotpink'], labels = ["No", "Yes"], shadow=True, explode=explode3, ax=ax2)

df.groupby('Live').size().plot(kind='pie', autopct=label_function, textprops={'fontsize': 15},
                                 colors=['mediumorchid', 'hotpink'], labels = ["No", "Yes"], shadow=True, explode=explode2, ax=ax3)

df.groupby('Job').size().plot(kind='pie', autopct=label_function, textprops={'fontsize': 15},
                                 colors=['mediumorchid', 'hotpink'], labels = ["No", "Yes"], shadow=True, explode=explode3, ax=ax4)

df.groupby('Divorce').size().plot(kind='pie', autopct=label_function, textprops={'fontsize': 15},
                                 colors=['mediumorchid', 'hotpink'], labels = ["No", "Yes"], shadow=True, explode=explode3, ax=ax5)

df.groupby('BankAc').size().plot(kind='pie', autopct=label_function, textprops={'fontsize': 15},
                                 colors=['mediumorchid', 'hotpink'], labels = ["No", "Yes"], shadow=True, explode=explode4, ax=ax6)

df.groupby('Business').size().plot(kind='pie', autopct=label_function, textprops={'fontsize': 15},
                                 colors=['mediumorchid', 'hotpink'], labels = ["No", "Yes"], shadow=True, explode=explode2, ax=ax7)

df.groupby('Contract').size().plot(kind='pie', autopct=label_function, textprops={'fontsize': 15},
                                 colors=['mediumorchid', 'hotpink'], labels = ["No", "Yes"], shadow=True, explode=explode1, ax=ax8)

df.groupby('TravelH').size().plot(kind='pie', autopct=label_function, textprops={'fontsize': 15},
                                 colors=['mediumorchid', 'hotpink'], labels = ["No", "Yes"], shadow=True, explode=explode1, ax=ax9)

df.groupby('TravelC').size().plot(kind='pie', autopct=label_function, textprops={'fontsize': 15},
                                 colors=['mediumorchid', 'hotpink'], labels = ["No", "Yes"], shadow=True, explode=explode5, ax=ax10)

df.groupby('WorkN').size().plot(kind='pie', autopct=label_function, textprops={'fontsize': 15},
                                 colors=['mediumorchid', 'hotpink'], labels = ["No", "Yes"], shadow=True, explode=explode5, ax=ax11)

df.groupby('JobDan').size().plot(kind='pie', autopct=label_function, textprops={'fontsize': 15},
                                 colors=['mediumorchid', 'hotpink'], labels = ["No", "Yes"], shadow=True, explode=explode1, ax=ax12)

df.groupby('JobInd').size().plot(kind='pie', autopct=label_function, textprops={'fontsize': 15},
                                 colors=['mediumorchid', 'hotpink'], labels = ["No", "Yes"], shadow=True, explode=explode1, ax=ax13)

df.groupby('Remarry').size().plot(kind='pie', autopct=label_function, textprops={'fontsize': 15},
                                 colors=['mediumorchid', 'hotpink'], labels = ["No", "Yes"], shadow=True, explode=explode1, ax=ax14)

ax1.set_xlabel('A woman can apply for a passport\n in the same way as a man', size=15, font='Lucida Sans Unicode')
ax2.set_xlabel('A woman can be head of household\n in the same way as a man', size=15, font='Lucida Sans Unicode')
ax3.set_xlabel('A woman can choose where to live\n in the same way as a man', size=15, font='Lucida Sans Unicode')
ax4.set_xlabel('A woman can get a job\n in the same way as a man', size=15, font='Lucida Sans Unicode')
ax5.set_xlabel('A woman can obtain a judgment of divorce\n in the same way as a man', size=15, font='Lucida Sans Unicode')
ax6.set_xlabel('A woman can open a bank account\n in the same way as a man', size=15, font='Lucida Sans Unicode')
ax7.set_xlabel('A woman can register a business\n in the same way as a man', size=15, font='Lucida Sans Unicode')
ax8.set_xlabel('A woman can sign a contract\n in the same way as a man', size=15, font='Lucida Sans Unicode')
ax9.set_xlabel('A woman can travel outside her home\n in the same way as a man', size=15, font='Lucida Sans Unicode')
ax10.set_xlabel('A woman can travel outside the country\n in the same way as a man', size=15, font='Lucida Sans Unicode')
ax11.set_xlabel('A woman can work at night\n in the same way as a man', size=15, font='Lucida Sans Unicode')
ax12.set_xlabel('A woman can work in a job deemed dangerous\n in the same way as a man', size=15, font='Lucida Sans Unicode')
ax13.set_xlabel('A woman can work in an industrial job\n in the same way as a man', size=15, font='Lucida Sans Unicode')
ax14.set_xlabel('A woman has the same rights to remarry\n in the same way as a man', size=15, font='Lucida Sans Unicode')

ax1.set_ylabel('', size=20)
ax2.set_ylabel('', size=20)
ax3.set_ylabel('', size=20)
ax4.set_ylabel('', size=20)
ax5.set_ylabel('', size=20)
ax6.set_ylabel('', size=20)
ax7.set_ylabel('', size=20)
ax8.set_ylabel('', size=20)
ax9.set_ylabel('', size=20)
ax10.set_ylabel('', size=20)
ax11.set_ylabel('', size=20)
ax12.set_ylabel('', size=20)
ax13.set_ylabel('', size=20)
ax14.set_ylabel('', size=20)

fig.tight_layout(pad=-35.0)
plt.tight_layout()
plt.show()
