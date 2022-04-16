import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RecapTableComponent } from './recap-table.component';

describe('RecapTableComponent', () => {
  let component: RecapTableComponent;
  let fixture: ComponentFixture<RecapTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RecapTableComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RecapTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
