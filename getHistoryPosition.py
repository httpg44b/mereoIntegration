def querySQL(conn):
    sql = """
    WITH cte AS (
    SELECT
         PFUNCAO.CODIGO
        ,CONVERT(VARCHAR(50), PFUNC.SALARIO) AS SALARIO
        ,PPESSOA.CODUSUARIO
        ,CONVERT(VARCHAR(10), ISNULL(PFUNC.DTULTIMOMOVIM, GETDATE()), 23) AS DTULTIMOMOVIM
        ,ROW_NUMBER() OVER (PARTITION BY PPESSOA.CODUSUARIO ORDER BY PFUNCAO.CODIGO DESC) AS rn
    FROM 
        PFUNCAO
    INNER JOIN
        PFUNC
        ON PFUNC.CODFUNCAO = PFUNCAO.CODIGO 
        AND PFUNC.CODCOLIGADA = PFUNCAO.CODCOLIGADA
    INNER JOIN
        PPESSOA
        ON PPESSOA.CODIGO = PFUNC.CODPESSOA
	WHERE 
	    CODUSUARIO <> 'null' AND CODSITUACAO <> 'D'
)
SELECT
     'ENG'+CODIGO AS 'CODIGO'
    ,SALARIO
    ,CODUSUARIO
    ,DTULTIMOMOVIM
FROM 
    cte
WHERE 
    rn = 1;
    """

    print('query sucessfully')

    cursor = conn.cursor()
    response = cursor.execute(sql)
    records = response.fetchall()

    return records