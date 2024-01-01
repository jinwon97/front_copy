import React, { useState } from 'react'
import { Box, Button, Grid } from '@mui/material'


const SectorsAnaly = () => {
    const [sector, setSector] = useState('')

    const sectors = [
      '한식음식점',
      '카페',
      '분식전문점',
      '간이주점',
      '치킨전문점',
      '중식음식점',
      '패스트푸드점',
      '제과점',
      '일식음식점',
      '양식음식점',
      '편의점',
      '일반의류',
      '화장품',
      '의약품',
      '일반교습학원',
      '미용실',
      '세탁소'
    ]

    const handleChange = (event) => {
      setSector(event.target.value);
    };
    function chicken() {
      return(
          <div>
              {
                  sector === '치킨전문점'
                  ? <p> HTML~ </p>
                  : null
              }
          </div>
      )
    }
    

  return (
    <>
    <Box sx = {{mt : 3, mb : 5 }}><h2>업종 선택</h2></Box>
    <Grid container spacing={2}>
      <Grid xs={2}>
      <item>
      {sectors.map((sector, idx) => {
        return <Button onClick={handleChange}>{sector}</Button>
      })}
      </item>
      </Grid>
    </Grid>
    <Button href = '#Report' size='large' variant="contained">분석 보기</Button>
    </>
  )
}

export default SectorsAnaly